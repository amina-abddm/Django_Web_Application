from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),              # /schedule/
    path('accueil/', views.home, name='accueil'),   # /schedule/accueil/
     
    # Connexion (login)
    path('login/', auth_views.LoginView.as_view(template_name='authentification/login.html'), name='login'),

    # Déconnexion (logout)
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Inscription (on va créer cette vue personnalisée)
    path('signup/', views.signup, name='signup'),
    
    # Dashboard pour les clients et les coachs
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Nouvelle URL prise de rendez-vous
    path('prendre-rdv/', views.prendre_rdv, name='prendre_rdv'),
    
    # Historique des séances pour les clients
    path('historique/', views.historique_client, name='historique_client'),

]

