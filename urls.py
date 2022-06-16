from django.urls import path
from .views import home, about, services, contact

app_name = "home"

urlpatterns = [
    path('', home, name="homeview"),
    path('about/', about, name="aboutview"),
    path('services/', services, name="servicesview"),
    path('contact/', contact, name="contactview"),
]