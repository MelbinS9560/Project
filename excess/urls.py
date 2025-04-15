from django.urls import path
from . import views

urlpatterns = [
    path('', views.excess_food_view, name='excess_page'),
]
