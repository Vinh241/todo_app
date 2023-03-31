
from django.contrib import admin
from django.urls import path,re_path
from menu import urls as todo_app
from django.conf.urls import include
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include(todo_app,namespace='todo_app')),
    re_path("",include('allauth.urls')),
]
