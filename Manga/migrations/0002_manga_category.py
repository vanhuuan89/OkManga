# Generated by Django 4.0.4 on 2022-06-09 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='category',
            field=models.ManyToManyField(to='Manga.category'),
        ),
    ]