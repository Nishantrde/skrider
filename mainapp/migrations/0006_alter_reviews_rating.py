# Generated by Django 4.2.10 on 2024-05-28 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_reviews_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
