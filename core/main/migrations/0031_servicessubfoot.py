# Generated by Django 4.1.4 on 2022-12-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_remove_servicesfoot_about_remove_servicesfoot_about1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesSubFoot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ServicesSuboot name')),
                ('about', models.TextField(verbose_name='ServicesSubFoot about')),
            ],
            options={
                'verbose_name': 'ServicesSubFoot',
                'verbose_name_plural': 'ServicesSubFoots',
            },
        ),
    ]