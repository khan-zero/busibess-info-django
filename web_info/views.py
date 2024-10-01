from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from .models import Hero, OurService, AboutUs, WhyUs, OurTeam, CustomerReviews

from random import randint
from colorama import Fore, init
init(autoreset=True)
# to install this  library: `pip3 install colorama

def index(request):
    # Getting all Hero objects
    hero = Hero.objects.all()
    
    # Handle empty queryset
    if not hero:
        random_object_hero = None
    else:
        # Getting a random number within the range of the queryset length
        random_item_hero = randint(0, hero.count() - 1)
        random_object_hero = hero[random_item_hero]

    # Fetching all services
    services = OurService.objects.all()

    # Getting AboutUs objects
    about = AboutUs.objects.all()
    
    # Handle empty queryset
    if not about:
        random_objects_about = None
    else:
        # Getting a random number within the range of the queryset length
        random_item_about = randint(0, about.count() - 1)
        random_objects_about = about[random_item_about]
      
    # Fetching all `why us` and our team
    why = WhyUs.objects.all()
    team = OurTeam.objects.all()

    # Prepare context for rendering
    context = {
        'hero': random_object_hero,
        'services': services,
        'about': random_objects_about,
        'why': why,
        'teams': team,
    }

    return render(request, "index.html", context)
    
def about(request):
    # Getting AboutUs objects
    about = AboutUs.objects.all()
    
    # Handle empty queryset
    if not about:
        random_objects_about = None
    else:
        # Getting a random number within the range of the queryset length
        random_item_about = randint(0, about.count() - 1)
        random_objects_about = about[random_item_about]
        
    return render(request, "about.html", {'about':random_objects_about})
    
def service(request):

    services = OurService.objects.all()
    return render(request, "service.html", {'services':services})
    
def why(request):

    why = WhyUs.objects.all()
    return render(request, "why.html", {'why':why})
    
def team(request):

    team = OurTeam.objects.all()
    return render(request, "team.html", {'teams':team})
    

"""
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')  # Redirect to your index page or stay on the same page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')  # Redirect to the index page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
    
"""
