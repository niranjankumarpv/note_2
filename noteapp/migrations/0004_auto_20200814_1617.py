# Generated by Django 3.1 on 2020-08-14 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0003_auto_20200814_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note_detail',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
