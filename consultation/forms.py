from django import forms

from .models import ConsultationRequest
class ConsultationForm(forms.ModelForm):
    class Meta:
        model = ConsultationRequest
        fields = '__all__'
        exclude = ['checked']