# Generated by Django 5.0.6 on 2024-05-21 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_todo_assigned_to_alter_todo_subtasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='assigned_to',
            field=models.ManyToManyField(null=True, to='api.contact'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='subtasks',
            field=models.ManyToManyField(null=True, to='api.subtask'),
        ),
    ]
