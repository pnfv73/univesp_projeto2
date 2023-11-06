from django.urls import path # [06/11/2023]
from .views import SignUpView # [06/11/2023]

# [06/11/2023]
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),   
]