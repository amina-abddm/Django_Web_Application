from django.shortcuts import render

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
