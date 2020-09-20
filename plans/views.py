from django.shortcuts import render
from .forms import CustomPlanForm


# Create your views here.


def plans(request):
    """A view to return the index page"""
    return render(request, 'plans/plans.html')

def custom_plans(request):
    """A view to return a custom plans page"""
    form= CustomPlanForm()

    return render(request, 'plans/custom_plan_form.html', {'form': form})


def surprise_plans(request):
    """A view to return the surprise plans page"""

    return render(request, 'plans/surprise_plan.html')
