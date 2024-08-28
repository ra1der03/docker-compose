from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAnimals),
    path('read/<str:pk>', views.getAnimal),
    path('create/', views.addAnimal),
    path('update/<str:pk>', views.updateAnimal),
    path('delete/<str:pk>', views.deleteAnimal),
]
