# Generated by Django 4.1.4 on 2022-12-28 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_aboutquality'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutquality',
            name='about1',
            field=models.TextField(blank=True, verbose_name='AboutQuality about1'),
        ),
    ]
