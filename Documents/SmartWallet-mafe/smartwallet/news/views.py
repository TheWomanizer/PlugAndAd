from django.shortcuts import render
from .models import News

def news(request):
    newss = News.objects.all().order_by('-date')
    
    # Simulación del monto de ahorros (puedes cambiarlo según la lógica de tu app)
    user_savings = 5000  

    return render(request, 'news/news.html', {'newss': newss, 'user_savings': user_savings})


