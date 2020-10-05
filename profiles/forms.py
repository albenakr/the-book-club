from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add custom labels
        """
        super().__init__(*args, **kwargs)
        self.fields['default_phone_number'].label = 'Phone Number'
        self.fields['default_postcode'].label = 'Postcode'
        self.fields['default_town_or_city'].label = 'Town or City'
        self.fields['default_street_address1'].label = 'Street Address 1'
        self.fields['default_street_address2'].label = 'Street Address 2'
        self.fields['default_county'].label = 'County, State or Locality'
