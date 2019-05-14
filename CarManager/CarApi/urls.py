from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.CarsApi.as_view()),
    path('cars/<int:pk>', views.CarDetail.as_view()),
    path('', views.homepage, name="homepage"),
    path('all', views.carspage, name="carpage")
]