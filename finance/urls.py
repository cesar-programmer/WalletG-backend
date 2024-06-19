"""
URL configuration for finance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from finance import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', views.user_list),
    path('api/users/<int:id>', views.user_detail),
    path('api/goals/', views.goals_list),
    path('api/goals/<int:id>', views.goals_detail),
    path('api/tips/', views.tips_list),
    path('api/tips/<int:id>', views.tips_detail),
    path('api/account/', views.account_list),
    path('api/account/<int:id>', views.account_detail),
]
