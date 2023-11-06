from django.contrib import admin
from django.urls import path, include # [06/11/2023]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('allauth.urls')), # [06/11/2023]
]
