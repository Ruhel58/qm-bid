from django import forms
from auction.models import Auction
from user_profile.models import Profile
from item.models import Item

class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['item', 'item_end_date']
        widgets = {
            'item_end_date': forms.DateTimeInput(attrs={'class': 'datetime-input'})
            }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(AuctionForm, self).__init__(*args, **kwargs)
        self.fields['item'].queryset = Item.objects.filter(seller=user)
        