from django.shortcuts import render

from nhl.models import NHLGame

# Create your views here.
def home(request):
    context = { }
    return render(request, "nhl/home.html", context)
