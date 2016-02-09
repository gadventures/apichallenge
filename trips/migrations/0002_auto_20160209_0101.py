# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 01:01
from __future__ import unicode_literals

from django.db import migrations, models

def load_fixture(apps, schema_editor):

	Store = apps.get_model("trips", "Trip")
	store_o = Store(id=0, name='Caribbean', start_date='2016-02-14', finish_date='2016-02-24', tour_capacity='20', package_price='2000', package_location='Cuba')
	store_o.save()
	store_t = Store(id=1, name='European', start_date='2016-04-10', finish_date='2016-04-20', tour_capacity='30', package_price='4000', package_location='France')
	store_t.save()
	store_h = Store(id=2, name='Great North', start_date='2016-08-17', finish_date='2016-08-27', tour_capacity='10', package_price='1000', package_location='Alaska')
	store_h.save()

class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='package_location',
            field=models.CharField(default='NA', max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='package_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='tour_capacity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        
        migrations.RunPython(load_fixture),
    ]

