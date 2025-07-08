# 🧘‍♀️ MyCoach – Application de Prise de Rendez-vous

MyCoach est une application web Django permettant à des clients de **prendre rendez-vous** en ligne avec un **coach** via un tableau de bord personnalisé.

---

## 🚀 Fonctionnalités

- 🔐 Authentification (inscription, connexion, déconnexion)
- 👤 Différenciation Coach / Client via groupes
- 🗓️ Prise de rendez-vous via formulaire
- 📋 Tableau de bord personnalisé :
  - Coach : accès à tous les rendez-vous
  - Client : accès uniquement à ses séances
- ✅ Validation des contraintes :
  - Un seul RDV à la fois
  - Plages horaires autorisées
  - Délai de 10 minutes entre deux RDV

---

## 🛠️ Technologies

- Python 3
- Django 5
- SQLite (par défaut)
- HTML, CSS (customisable)
- Templates Django

---

## 📂 Structure

```bash
mycoach/
│
├── manage.py # Commande principale Django
├── db.sqlite3 # Base de données SQLite
├── README.md # Documentation du projet
├── requirements.txt # Dépendances (à générer avec pip freeze > requirements.txt)
│
├── mycoach/ # Configuration principale du projet Django
│ ├── init.py
│ ├── settings.py # Paramètres globaux du projet
│ ├── urls.py # Routes principales du projet
│ ├── wsgi.py
│ └── asgi.py
│
├── schedule/ # Application principale "schedule"
│ ├── migrations/ # Fichiers de migration pour la BDD
│ │ └── init.py
│ ├── templates/ # Dossiers des templates HTML
│ │ └── schedule/
│ │ ├── base.html
│ │ ├── home.html
│ │ ├── dashboard_client.html
│ │ ├── dashboard_coach.html
│ │ ├── prise_rdv.html
│ │ └── authentification/
│ │ ├── login.html
│ │ ├── signup.html
│ │ └── logout.html
│ ├── init.py
│ ├── admin.py # Enregistrement des modèles dans l'admin
│ ├── apps.py
│ ├── forms.py # Formulaires personnalisés
│ ├── models.py # Modèles (ex: Seance)
│ ├── tests.py
│ └── views.py # Logique des vues (dashboard, prise de rendez-vous, etc.)

```

---

## 🧑‍💻 Installation et lancement

1. **Cloner le projet**

```bash
git clone https://github.com/tonprofil/mycoach.git
cd mycoach
```

2. **Créer un environnement virtuel**

```bash
python -m venv .venv
source .venv/bin/activate  # Sur Windows : .venv\Scripts\activate
```

3. **Installer les dépendances**

```bash
pip install django
```

4. **Migrer la base de données**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Créer un superutilisateur**

```bash
python manage.py createsuperuser
```

6. **Lancer le serveur**

```bash
python manage.py runserver
```

**➡️ Accédez à l'application via : http://127.0.0.1:8000/schedule/accueil/**

---

## ✅ Accès Admin

**➡️ Visitez : http://127.0.0.1:8000/admin/**

Ajoutez un groupe coach et associez les utilisateurs coach à ce groupe.

---

## ✨Améliorations possibles

- Ajouter des notifications email
- Calendrier dynamique avec disponibilité
- Design responsive & amélioré
- Historique des séances pour le client

