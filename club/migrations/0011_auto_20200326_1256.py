# Generated by Django 3.0.3 on 2020-03-26 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0010_auto_20200326_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complete',
            old_name='end_date',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='complete',
            name='start_date',
        ),
    ]