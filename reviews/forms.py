from django.forms import ModelForm
from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'title', 'review_text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['review_text'].label = "Your Review"

