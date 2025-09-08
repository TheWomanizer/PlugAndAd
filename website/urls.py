from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('signup/', views.signup, name='signup'),
    path('packages/', views.packages, name='packages'),
    
    # About section with sub-pages
    path('about/', views.about, name='about'),
    path('about/mission/', views.about_mission, name='about_mission'),
    path('about/team/', views.about_team, name='about_team'),
    path('about/privacy/', views.about_privacy, name='about_privacy'),
    path('about/terms/', views.about_terms, name='about_terms'),
    path('about/contact/', views.about_contact, name='about_contact'),
]