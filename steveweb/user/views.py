from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

@login_required
def home(request):
    context = { } 
    return render(request, "user/home.html", context)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "user/signup.html"
    success_url = reverse_lazy('user_home')
