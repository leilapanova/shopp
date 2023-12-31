from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('create/', create, name='create'),
    path('product/<int:id>', product, name='product'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]
