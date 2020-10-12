from django.urls import path
from . import views

urlpatterns = [
    path('addneedy/',views.addneedy,name="addneedy"),
    path('needy/',views.needy,name="needy")
    
]
