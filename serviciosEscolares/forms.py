from django import forms
from serviciosEscolares.models import *


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = '__all__'