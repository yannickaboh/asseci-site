from django import forms
from .models import Evenement
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab
from django.contrib.auth.models import User

from .models import Evenement, Post



#  your forms.



class EvenementForm(forms.ModelForm):

    class Meta:
        model = Evenement
        fields = ['evenement', 'lieu', 'dateCreation', 'jour', 'heure', 'hDebut', 'hFin', 
        'contact', 'nbreParticipants', 'bureau', 'odd1', 'odd2', 'odd3', 'odd4', 'odd5', 
        'odd6', 'odd7', 'odd8', 'odd9', 'odd10' ]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]