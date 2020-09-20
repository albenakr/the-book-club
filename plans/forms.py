from django import forms
from products.models import Genre, Language

class CustomPlanForm(forms.Form):
    CHOICES = (
        (3, '3 months'),
        (6, '6 months'),
        (12, '12 months'),
    )
    name = forms.CharField(label='Name your plan', max_length=454)
    genres = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=Genre.objects.all())
    languages = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=Language.objects.all())
    plan_duration = forms.ChoiceField(choices=CHOICES)


