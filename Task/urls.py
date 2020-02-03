from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin', admin.site.urls),
    path('premium/', include('premium.urls')),
    path('rider_premium/', include('rider_premium.urls')),
    path('freelook/', include('freelook.urls'))
]
