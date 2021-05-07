from django.urls import path
from fbv import views

urlpatterns = [
    path('', views.author),
    path('author/<int:pk>', views.author_details),
]