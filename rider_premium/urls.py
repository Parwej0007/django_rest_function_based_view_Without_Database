from django.urls import path
from .views import rider_premium

urlpatterns = [
    path('', rider_premium, name='rider_view_url'),
]
