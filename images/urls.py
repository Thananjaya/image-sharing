from django.urls import path
from . import views

urlpatterns = [
	path('new/', views.image_create, name="create"),
]