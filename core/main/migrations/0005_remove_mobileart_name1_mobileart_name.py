# Generated by Django 4.1.4 on 2022-12-27 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_mobileart_name_mobileart_about2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobileart',
            name='name1',
        ),
        migrations.AddField(
            model_name='mobileart',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='MobileArt name'),
        ),
    ]
