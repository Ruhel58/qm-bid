from django.db import models
from user_profile.models import Profile


class Item(models.Model):
    # ForeignKey relationship with user so that many items can be related to a user
    # https://docs.djangoproject.com/en/2.2/topics/db/examples/many_to_one/
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=450)
    starting_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.01)
    image = models.ImageField(upload_to='item_images', default='default.jpg', null=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def to_float(self, val):
        return float(val)

    def __str__(self):
        return 'Item: %s' % (self.title)

    def to_dict(self):
        data = {
            'title' : self.title,
            'description': self.description,
            'starting_price': float(self.starting_price),
            'seller' : self.seller.to_dict(),
        }
        return data



#bcrytp
#pillow