# Generated by Django 4.1.4 on 2022-12-26 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeadParallo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='HeadParallo name')),
                ('name1', models.CharField(max_length=30, verbose_name='HeadParallo name1')),
                ('name2', models.CharField(max_length=30, verbose_name='HeadParallo name2')),
                ('name3', models.CharField(max_length=30, verbose_name='HeadParallo name3')),
                ('name4', models.CharField(max_length=30, verbose_name='HeadParallo name4')),
                ('name5', models.CharField(max_length=30, verbose_name='HeadParallo name5')),
                ('about', models.TextField(verbose_name='HeadParallo about')),
            ],
            options={
                'verbose_name': 'HeadParallo',
                'verbose_name_plural': 'HeadParallos',
            },
        ),
    ]
