# Generated by Django 4.1.4 on 2022-12-27 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_mobileart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobileart',
            name='about1',
            field=models.TextField(null=True, verbose_name='MobileArt about1'),
        ),
    ]