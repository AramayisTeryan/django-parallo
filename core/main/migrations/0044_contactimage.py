# Generated by Django 4.1.4 on 2022-12-31 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_contactparallo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='ContactImage image')),
            ],
            options={
                'verbose_name': 'ContactImage',
                'verbose_name_plural': 'ContactImages',
            },
        ),
    ]
