"""
URL configuration for responsive project.

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
from app1.views import *



from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('website/', website, name='website'),
    path('anime_list/', anime_list, name='anime_list'),
    path('anime_list_2/', anime_list_2, name='anime_list_2'),
    path('anime_list_3/', anime_list_3, name='anime_list_3'),
    path('ongoing/', ongoing, name='ongoing'),
    path('ongoing_2/', ongoing_2, name='ongoing_2'),
    path('upcoming/', upcoming, name='upcoming'),
    path('upcoming_2/', upcoming_2, name='upcoming_2'),
    path('completed/', completed, name='completed'),
    path('web_2/', web_2, name='web_2'),
    path('web_3/', web_3, name='web_3'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('password/', password, name='password'),
    path('submit-login/', submit_login, name='submit_login'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    path('fetch_anime_data/', fetch_anime_data, name='fetch_anime_data'),
     path('anime_search/', anime_search, name='anime_search'),
     path('anime/<int:anime_id>/', anime_detail, name='anime_detail'),
]