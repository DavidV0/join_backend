# Generated by Django 5.0.6 on 2024-05-22 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_todo_subtasks_subtask_parent_task_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]