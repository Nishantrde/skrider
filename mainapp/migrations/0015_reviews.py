# Generated by Django 4.2.10 on 2024-05-28 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20240528_0902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('review', models.CharField(max_length=255)),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]