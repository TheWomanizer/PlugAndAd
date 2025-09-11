from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .models import UserProfile, Package, CartItem, Purchase, PurchaseItem, UserPackage


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'auth_app/login.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        
        if password != password_confirm:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, 'auth_app/signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
            return render(request, 'auth_app/signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El email ya está registrado')
            return render(request, 'auth_app/signup.html')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Crear perfil de usuario con prueba gratuita
        profile = UserProfile.objects.create(
            user=user,
            subscription_plan='trial',
            subscription_end_date=timezone.now() + timedelta(days=14)
        )
        
        login(request, user)
        messages.success(request, 'Cuenta creada exitosamente')
        return redirect('dashboard')
    
    return render(request, 'auth_app/signup.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente')
    return redirect('home')


@login_required
def dashboard_view(request):
    # Crear perfil si no existe
    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'subscription_plan': 'trial',
            'subscription_end_date': timezone.now() + timedelta(days=14)
        }
    )
    
    # Obtener paquetes del usuario
    user_packages = UserPackage.objects.filter(user=request.user, is_active=True)
    
    return render(request, 'auth_app/dashboard.html', {
        'user': request.user,
        'profile': profile,
        'user_packages': user_packages
    })


@login_required
def cart_view(request):
    # Obtener items del carrito desde la base de datos
    cart_items = CartItem.objects.filter(user=request.user)
    
    return render(request, 'auth_app/cart.html', {
        'user': request.user,
        'cart_items': cart_items
    })


@login_required
def profile_view(request):
    # Crear perfil si no existe
    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'subscription_plan': 'trial',
            'subscription_end_date': timezone.now() + timedelta(days=14)
        }
    )
    
    if request.method == 'POST':
        # Update user profile
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()
        messages.success(request, 'Perfil actualizado exitosamente')
        return redirect('profile')
    
    # Obtener historial de compras
    purchases = Purchase.objects.filter(user=request.user).order_by('-created_at')
    
    return render(request, 'auth_app/profile.html', {
        'user': request.user,
        'profile': profile,
        'purchases': purchases
    })


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        package_id = request.POST.get('package_id')
        
        try:
            package = Package.objects.get(id=package_id)
            cart_item, created = CartItem.objects.get_or_create(
                user=request.user,
                package=package,
                defaults={'quantity': 1}
            )
            
            if not created:
                cart_item.quantity += 1
                cart_item.save()
            
            return JsonResponse({
                'success': True,
                'message': 'Paquete agregado al carrito'
            })
        except Package.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Paquete no encontrado'
            })
    
    return JsonResponse({'success': False, 'message': 'Método no permitido'})


@login_required
def remove_from_cart(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')
        
        try:
            cart_item = CartItem.objects.get(id=cart_item_id, user=request.user)
            cart_item.delete()
            
            return JsonResponse({
                'success': True,
                'message': 'Paquete eliminado del carrito'
            })
        except CartItem.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Item no encontrado'
            })
    
    return JsonResponse({'success': False, 'message': 'Método no permitido'})
