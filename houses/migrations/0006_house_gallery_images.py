# Generated by Django 5.1.1 on 2024-12-08 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0005_delete_housegallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='gallery_images',
            field=models.JSONField(default=list),
        ),
    ]