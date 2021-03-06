from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new_cadastro', views.post_cad, name='post_cad'),
    path('post/cadastro', views.cad_list, name='cad_list'),
    path('post/edit_cadastro', views.cad_detail, name='cad_detail'),
]