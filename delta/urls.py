from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='delta-home'),
    path('about/', views.about, name='delta-about'),
]