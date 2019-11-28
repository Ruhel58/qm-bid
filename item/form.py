from django import forms
from item.models import Item
from user_profile.models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description','starting_price','image']
    