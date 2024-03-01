"""University URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from main.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('letters/', LetterListCreateView),
    path('letters/<int:pk>/', LetterRetrieveUpdateDestroyView),
    path("create_student/",create_student),
    path("check_ielts_score/",check_ielts_score),
    path("create_category",create_category),
    path("create_degree",create_degree),
    path("create_direction",create_direction),
    path("register_at_university",register_at_university),
    path('create_university',create_university),
    path("edit_profile",edit_profile),
    path("create_studentlist",create_studentlist),
    path("create_popular_university",create_popular_university),
    path("my_filter",my_filter),
    path("HowWeWorkRetrieveUpdateDestroyView",HowWeWorkRetrieveUpdateDestroyView),
    path("loged_students",loged_students)
    ]
