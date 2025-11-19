from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('greet/<str:name>/', views.greet, name="greet"),
    path('info/', views.info_json, name="info_json"),
    path('page/', views.index, name="index"),
    path('calc/', views.calc, name="calc"),
]