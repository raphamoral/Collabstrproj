from django.urls import path
from . import views

urlpatterns = [
    path('contents/', views.content_list, name='content_list'),
    path('filter_content/', views.filter_content, name='filter_content'),

]