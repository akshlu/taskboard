# Generated by Django 2.0.5 on 2018-05-09 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='epic',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='epic',
            name='name',
            field=models.TextField(default='No Name'),
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.TextField(default='No Name'),
        ),
        migrations.AddField(
            model_name='subtask',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='subtask',
            name='name',
            field=models.TextField(default='No Name'),
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.TextField(default='No Name'),
        ),
    ]