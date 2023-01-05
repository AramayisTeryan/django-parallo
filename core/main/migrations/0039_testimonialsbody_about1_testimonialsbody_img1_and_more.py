# Generated by Django 4.1.4 on 2022-12-30 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_testimonialsbody'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonialsbody',
            name='about1',
            field=models.TextField(null=True, verbose_name='Testimonials about1'),
        ),
        migrations.AddField(
            model_name='testimonialsbody',
            name='img1',
            field=models.ImageField(null=True, upload_to='media', verbose_name='TestimonialsBody image1'),
        ),
        migrations.AddField(
            model_name='testimonialsbody',
            name='name1',
            field=models.CharField(max_length=30, null=True, verbose_name='TestimonialsBody name1'),
        ),
    ]