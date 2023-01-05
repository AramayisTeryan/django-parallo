# Generated by Django 4.1.4 on 2022-12-27 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_homebody'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeFoot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='HomeFoot name')),
                ('about', models.TextField(verbose_name='HomeFoot about')),
                ('about1', models.TextField(verbose_name='HomeFoot about1')),
                ('img', models.ImageField(upload_to='media', verbose_name='HomeFoot image')),
            ],
            options={
                'verbose_name': 'HomeFoot',
                'verbose_name_plural': 'HomeFoots',
            },
        ),
    ]
