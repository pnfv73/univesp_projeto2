from django.contrib import admin
from django.urls import path, include # [06/11/2023]
from django.views.generic.base import TemplateView # [06/11/2023]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('allauth.urls')), # [06/11/2023]
    path("contas/", include("contas.urls")), # [06/11/2023]
    path("", TemplateView.as_view(template_name="home.html"), name="home"), # [06/11/2023]
]