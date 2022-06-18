# Generated by Django 4.0.3 on 2022-06-18 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('index', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('modified_date', models.CharField(max_length=50)),
                ('views', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('thumbnail', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
                ('author', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(default='A great manga', max_length=200)),
                ('views', models.PositiveIntegerField(default=0)),
                ('chapters_number', models.PositiveIntegerField(default=0)),
                ('summary', models.CharField(max_length=1000)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='Manga.category')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('comment', models.CharField(max_length=200)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manga.chapter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('index', models.PositiveSmallIntegerField()),
                ('link', models.URLField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manga.chapter')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='manga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manga.manga'),
        ),
    ]
