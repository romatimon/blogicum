# Generated by Django 3.2.16 on 2023-08-09 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230809_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Фото'),
        ),
    ]
