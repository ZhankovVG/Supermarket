from django import forms
from .models import  *


class RatingForm(forms.ModelForm):
    # Форма добавления рейтинга
    star = forms.ModelChoiceField(
        queryset=RetingsStar.objects.all(), widget=forms.RadioSelect(),
        empty_label=None
    )

    class Meta:
        model = Reting
        fields = ('star',)