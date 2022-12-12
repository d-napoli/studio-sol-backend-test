from django.contrib import admin
from django.urls import path

from app import view_main

urlpatterns = [
    path("admin/", admin.site.urls),
    path("verify/", view_main.verify_password),
]
