# Generated by Django 3.0.5 on 2021-04-22 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210422_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='category',
        ),
        migrations.AddField(
            model_name='title',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Выберите категорию', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='api.Category', verbose_name='Категория'),
        ),
        migrations.RemoveField(
            model_name='title',
            name='genre',
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, help_text='Выберите жанр', null=True, related_name='titles', to='api.Genre', verbose_name='Жанр'),
        ),
    ]
