from django.urls import path

from . import views
app_name="frontuser"

urlpatterns = [
    path('', views.home, name='home'),
    path('registration', views.registration, name="registration")
    
]
