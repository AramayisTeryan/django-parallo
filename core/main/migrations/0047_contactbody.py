# Generated by Django 4.1.4 on 2022-12-31 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_contact_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ContactBody name')),
                ('about', models.TextField(verbose_name='ContactBody about')),
                ('about1', models.TextField(verbose_name='ContactBody about1')),
            ],
            options={
                'verbose_name': 'ContactBody',
                'verbose_name_plural': 'ContactBodies',
            },
        ),
    ]
