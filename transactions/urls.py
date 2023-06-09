from django.urls import path
from . import views

app_name = "transactions"
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('view', views.view, name='view'),
    path('reports', views.reports, name='reports'),
    path('counterapi', views.counterapi, name='counterapi')
]