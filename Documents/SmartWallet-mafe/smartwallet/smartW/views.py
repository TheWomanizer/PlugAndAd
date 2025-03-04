from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from .models import Saving

# Create your views here.

def dashboard (request):
    total_saving= Saving.objects.aggregate(total= Sum('amount'))['total'] or 0
    return render(request, 'savings/dashboard.html', {'total_savings': total_saving})