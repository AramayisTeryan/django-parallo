# Generated by Django 4.1.4 on 2022-12-30 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_servicesbody'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesFoot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ServicesFoot name')),
                ('name1', models.CharField(max_length=50, verbose_name='ServicesFoot name1')),
                ('name2', models.CharField(max_length=50, verbose_name='ServicesFoot name2')),
                ('name3', models.CharField(max_length=50, verbose_name='ServicesFoot name3')),
                ('name4', models.CharField(max_length=50, verbose_name='ServicesFoot name4')),
                ('name5', models.CharField(max_length=50, verbose_name='ServicesFoot name5')),
                ('about', models.TextField(verbose_name='ServicesFoot about')),
                ('about1', models.TextField(verbose_name='ServicesFoot about1')),
                ('about2', models.TextField(verbose_name='ServicesFoot about2')),
            ],
            options={
                'verbose_name': 'ServicesFoot',
                'verbose_name_plural': 'ServicesFoots',
            },
        ),
    ]
