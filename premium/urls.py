from django.urls import path
from .views import premium

urlpatterns = [
    path('', premium, name='premium_urls'),
]
