from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from sixfournine.models import Ticket

# Create your views here.
def home(request):
    all_tickets = Ticket.objects.all()
    context = { 'all_tickets': all_tickets } 
    return render(request, "sixfournine/home.html", context)

