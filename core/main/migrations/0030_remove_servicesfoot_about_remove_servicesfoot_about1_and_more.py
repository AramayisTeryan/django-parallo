# Generated by Django 4.1.4 on 2022-12-30 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_servicesfoot_name1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicesfoot',
            name='about',
        ),
        migrations.RemoveField(
            model_name='servicesfoot',
            name='about1',
        ),
        migrations.AddField(
            model_name='servicesfoot',
            name='name2',
            field=models.CharField(max_length=50, null=True, verbose_name='ServicesFoot name2'),
        ),
    ]