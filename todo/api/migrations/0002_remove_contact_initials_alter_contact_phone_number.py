# Generated by Django 5.0.6 on 2024-05-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='initials',
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]