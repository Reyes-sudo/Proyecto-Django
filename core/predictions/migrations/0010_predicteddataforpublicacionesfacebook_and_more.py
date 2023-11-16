# Generated by Django 4.1.7 on 2023-11-02 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0009_predicteddatatensorflowmodel_image_compare_results'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictedDataForPublicacionesFacebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio_referencia', models.CharField(blank=True, max_length=100, null=True)),
                ('image_predicted_7_days', models.ImageField(blank=True, null=True, upload_to='predicted_images_publicaciones')),
                ('image_validate_model', models.ImageField(blank=True, null=True, upload_to='validated_images_publicaciones')),
                ('image_compare_results', models.ImageField(blank=True, null=True, upload_to='compare_images_publicaciones')),
            ],
        ),
        migrations.CreateModel(
            name='PredictedPublicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predicted_data_for_public', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predictions.predicteddataforpublicacionesfacebook')),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predictions.publicacionesfacebook')),
            ],
        ),
    ]
