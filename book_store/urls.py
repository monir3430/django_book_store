from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('store_new/', views.store, name='store_new'),
    path('show_book/', views.show_book, name='show_book')
]