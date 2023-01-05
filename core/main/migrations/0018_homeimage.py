# Generated by Django 4.1.4 on 2022-12-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_aboutimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='HomeImage image')),
            ],
            options={
                'verbose_name': 'HomeImage',
                'verbose_name_plural': 'HomeImages',
            },
        ),
    ]
