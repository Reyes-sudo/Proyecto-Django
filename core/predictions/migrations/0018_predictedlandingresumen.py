# Generated by Django 4.1.7 on 2023-11-03 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0017_predictedprophetlandingmodel_image_feed_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictedLandingResumen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landing_less_high', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='landing_less_high', to='predictions.landingpageusuarios')),
                ('landing_less_low', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='landing_less_low', to='predictions.landingpageusuarios')),
                ('landing_most', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='landing_most', to='predictions.landingpageusuarios')),
            ],
        ),
    ]
