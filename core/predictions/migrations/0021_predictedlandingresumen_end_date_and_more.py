# Generated by Django 4.1.7 on 2023-11-03 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0020_remove_predictedlandingresumen_landing_less_high_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictedlandingresumen',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='predictedlandingresumen',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]