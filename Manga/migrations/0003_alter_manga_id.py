# Generated by Django 4.0.4 on 2022-06-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manga', '0002_manga_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]