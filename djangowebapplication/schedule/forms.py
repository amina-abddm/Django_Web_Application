from django import forms
from .models import Seance
from django.utils import timezone
from datetime import timedelta

class SeanceForm(forms.ModelForm):
    class Meta:
        model = Seance
        fields = ['date', 'heure_debut', 'objet']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'heure_debut': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        heure_debut = cleaned_data.get('heure_debut')

        # Vérifie que le rendez-vous est dans le futur
        if date and heure_debut:
            datetime_rdv = timezone.make_aware(
                timezone.datetime.combine(date, heure_debut)
            )
            if datetime_rdv < timezone.now():
                raise forms.ValidationError("Le rendez-vous doit être dans le futur.")

        # Ajoute d’autres règles si nécessaire (ex. horaires autorisés, délai de 10 minutes, etc.)
        return cleaned_data
