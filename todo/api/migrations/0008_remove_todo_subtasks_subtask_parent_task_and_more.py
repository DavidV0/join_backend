# Generated by Django 5.0.6 on 2024-05-22 13:31

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_todo_assigned_to_remove_todo_subtasks_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='subtasks',
        ),
        migrations.AddField(
            model_name='subtask',
            name='parent_task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='api.todo'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]