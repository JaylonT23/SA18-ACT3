from django.urls import path
from myapp import views

urlpatterns = [
    path('products/', views.index, name='index'),
    path('products/<int:id>/', views.show, name='show'),
]
