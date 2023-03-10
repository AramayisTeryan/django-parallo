# Generated by Django 4.1.4 on 2022-12-31 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_testimonialsfoot'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactParallo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='ContactParallo name')),
                ('name1', models.CharField(max_length=30, verbose_name='ContactParallo name1')),
                ('name2', models.CharField(max_length=30, verbose_name='ContactParallo name2')),
                ('name3', models.CharField(max_length=30, verbose_name='ContactParallo name3')),
                ('name4', models.CharField(max_length=30, verbose_name='ContactParallo name4')),
                ('name5', models.CharField(max_length=30, verbose_name='ContactParallo name5')),
                ('about', models.TextField(verbose_name='ContactParallo about')),
            ],
            options={
                'verbose_name': 'ContactParallo',
                'verbose_name_plural': 'ContactParallos',
            },
        ),
    ]
