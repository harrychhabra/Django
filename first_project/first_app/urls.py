from django.conf.urls import url
from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.homepage,name="index"),
    path('login/',views.login,name = "index"),
    path('Homepage/',views.checkHtml,name="index"),
]