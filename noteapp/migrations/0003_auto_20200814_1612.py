# Generated by Django 3.1 on 2020-08-14 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0002_note_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='text',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='note_detail',
            old_name='text',
            new_name='description',
        ),
    ]