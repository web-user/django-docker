# Generated by Django 2.0.1 on 2018-01-31 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20180126_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='todo',
        ),
        migrations.AddField(
            model_name='todo',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todo.Project'),
            preserve_default=False,
        ),
    ]