"""
URL configuration for ebooksite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ebookapp import views

urlpatterns = [
    path('category-list/', views.category_list, name='category_list'),
    path('books/', views.book_list, name='book_list_all'),  # All books
    path('books/category/<int:category_id>/', views.book_list, name='book_list_category'),  # Filtered by category
    path('books/subcategory/<int:subcategory_id>/', views.book_list, name='book_list_subcategory'),
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about, name="about"),
    path('', views.index, name="index"),
    
    
]
