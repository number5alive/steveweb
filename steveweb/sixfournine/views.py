from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context = { } 
    return render(request, "sixfournine/home.html", context)

