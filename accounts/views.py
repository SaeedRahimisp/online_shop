from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import UserCreationForm

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
