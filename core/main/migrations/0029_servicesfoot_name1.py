# Generated by Django 4.1.4 on 2022-12-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_servicesfoot_about1'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicesfoot',
            name='name1',
            field=models.CharField(max_length=50, null=True, verbose_name='ServicesFoot name1'),
        ),
    ]