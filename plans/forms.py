from django import forms
from products.models import Genre, Language
from plans.models import PlanDuration

class CustomPlanForm(forms.Form):
    name = forms.CharField(label='Name your plan', max_length=454)
    genres = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Genre.objects.all())
    languages = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Language.objects.all())
    plan_duration = forms.ModelChoiceField(widget=forms.CheckboxSelectMultiple, queryset=PlanDuration.objects.all())
