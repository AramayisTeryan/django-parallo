# Generated by Django 4.1.4 on 2022-12-27 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_mobileart_about1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobileart',
            name='name',
        ),
        migrations.AddField(
            model_name='mobileart',
            name='about2',
            field=models.TextField(null=True, verbose_name='MobileArt about2'),
        ),
    ]
