from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.timezone import make_aware
from .models import Seance

class SeanceForm(forms.ModelForm):
    class Meta:
        model = Seance
        fields = ['date', 'heure_debut', 'objet']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'heure_debut': forms.TimeInput(attrs={'type': 'time'}),
            'objet': forms.Textarea(attrs={'rows': 2}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        heure_debut = cleaned_data.get('heure_debut')
        objet = cleaned_data.get('objet')

        if date and heure_debut:
            # Combiner date et heure pour créer un datetime complet
            datetime_rdv = make_aware(timezone.datetime.combine(date, heure_debut))

            # 1. Le rendez-vous doit être dans le futur
            if datetime_rdv < timezone.now():
                raise ValidationError("Le rendez-vous doit être prévu dans le futur.")

            # 2. Les rendez-vous doivent être entre 9h et 18h
            if not (9 <= heure_debut.hour < 18):
                raise ValidationError("Les rendez-vous doivent être pris entre 9h et 18h.")

            # 3. Vérifie s’il y a déjà un rendez-vous à cette date et heure
            if Seance.objects.filter(date=date, heure_debut=heure_debut).exists():
                raise ValidationError("Un rendez-vous existe déjà à cet horaire.")

            # 4. Vérifie qu’il y a au moins 10 minutes entre les rendez-vous du même jour
            rdvs_du_jour = Seance.objects.filter(date=date)
            for rdv in rdvs_du_jour:
                delta_minutes = abs((rdv.heure_debut.hour * 60 + rdv.heure_debut.minute) -
                                    (heure_debut.hour * 60 + heure_debut.minute))
                if delta_minutes < 10:
                    raise ValidationError("Il doit y avoir au moins 10 minutes entre deux rendez-vous.")

        return cleaned_data
