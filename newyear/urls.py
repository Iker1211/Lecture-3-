from django.urls import path # import path function
from . import views # import views.py

urlpatterns = [
    path("", views.index, name="index") # when user goes to the root URL, call the index function in views.py
]