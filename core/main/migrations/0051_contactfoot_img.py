# Generated by Django 4.1.4 on 2022-12-31 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_contactfoot'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactfoot',
            name='img',
            field=models.ImageField(null=True, upload_to='media', verbose_name='ContactFoot image'),
        ),
    ]