from django import forms
from .models import  *


class RatingForm(forms.ModelForm):
    # Форма добавления рейтинга
    star = forms.ModelChoiceField(
        queryset=RatingsStar.objects.all(), widget=forms.RadioSelect(),
        empty_label=None
    )

    class Meta:
        model = Rating
        fields = ('star',)


class CommentsForm(forms.ModelForm):
    # добавление коментария
    class Meta:
        model = Comments
        fields = (
            'name', 'text', 'email'
        )
            
        