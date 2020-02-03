from django.urls import path
from .views import freelook

urlpatterns = [
    path('', freelook, name='freelook_urls'),
]
