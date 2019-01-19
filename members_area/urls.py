from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="landing-page"),
    path('home', views.home, name="home-page"),
    path('garage', views.garage, name="garage-page"),
    path('events', views.events, name="events-page"),
    path('pricing', views.pricing, name="pricing-page"),
]
