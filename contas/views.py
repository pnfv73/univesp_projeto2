# [06/11/2023]
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    #success_url = reverse_lazy("login")
    template_name = "contas/signup.html"