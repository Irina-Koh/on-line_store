from django.urls import path
from catalog import views
from catalog.apps import NewappConfig


app_name = NewappConfig.name

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
]
