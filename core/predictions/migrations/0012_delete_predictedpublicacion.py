# Generated by Django 4.1.7 on 2023-11-02 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0011_predicteddataforpublicacionesfacebook_publications'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PredictedPublicacion',
        ),
    ]
