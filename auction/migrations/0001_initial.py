# Generated by Django 2.1 on 2019-11-28 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '0001_initial'),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_end_date', models.DateField(max_length=8)),
                ('current_bid', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('active', models.BooleanField(default=True)),
                ('highest_bidder', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to='user_profile.Profile')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Item')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='user_profile.Profile')),
                ('winner', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='user_profile.Profile')),
            ],
        ),
    ]
