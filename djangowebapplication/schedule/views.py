from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.

def home(request):
    # On peut envoyer des informations au template via un dictionnaire (contexte)
    context = {
        'coach_name': 'Jean Dupont',
        'services': [
            'Coaching individuel',
            'Ateliers de groupe',
            'Suivi en ligne',
        ],
        'hours': 'Lundi à Vendredi, 9h - 18h',
    }
    return render(request, 'schedule/home.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'authentification/signup.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.groups.filter(name='coach').exists():
        return render(request, 'schedule/dashboard_coach.html')
    else:
        return render(request, 'schedule/dashboard_client.html')

