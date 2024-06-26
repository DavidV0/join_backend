# Generated by Django 5.0.6 on 2024-05-20 09:40

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=70)),
                ('phone_number', models.IntegerField(max_length=20)),
                ('initials', models.CharField(max_length=2)),
                ('badge_color', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('state', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('due_date', models.DateField(default=datetime.date.today, verbose_name=())),
                ('category', models.CharField(max_length=50)),
                ('prio', models.PositiveSmallIntegerField(default=1)),
                ('status', models.CharField(max_length=40)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.contact')),
                ('subtasks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subtask')),
            ],
        ),
    ]
