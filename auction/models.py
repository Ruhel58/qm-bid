from django.db import models
from item.models import Item
from user_profile.models import Profile
import datetime

class Auction(models.Model):
    # this is a weak entity
    # one to one with item so on delete of item, auction deletes
    # https://docs.djangoproject.com/en/2.2/topics/db/examples/one_to_one/
    item_end_date = models.DateField(max_length=8)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="seller")
    current_bid = models.DecimalField(default=0.00, decimal_places=2, max_digits=8)
    highest_bidder = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, default=None, related_name="bidder", blank=True)
    active = models.BooleanField(default=True)
    winner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, default=None, related_name="winner", blank=True)

    def __str__(self):
        return '%s ending on %s' % (self.item.title, self.item_end_date)

    def update_active(self):
        if datetime.date.today() > self.item_end_date:
            self.active = False
            self.winner = self.highest_bidder
            self.save()

    def to_dict(self):
        data = {
            'id' : self.id,
            'active' : self.active,
            'item' : self.item.to_dict(),
            'seller' : self.seller.to_dict(),
            'current_bid' : float(self.current_bid),
            'item_end_date' : str(self.item_end_date),
            'highest_bidder' : None,
            'winner' : None
        }

        if self.highest_bidder:
            data.update(highest_bidder = self.highest_bidder.to_dict())
      
        if self.winner:
            data.update(winner = self.winner.to_dict())

        return data

        