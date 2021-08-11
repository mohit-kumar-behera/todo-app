from django.urls import path,include
from .import views

app_name = 'home'

urlpatterns = [
    path('',views.home,name="home"),
    path('statistics/',views.statistics,name="statistics"),
    path('toggle/',views.toggleTask,name='toggle'),
    path('createTask/',views.createTask,name="createTask")
]
