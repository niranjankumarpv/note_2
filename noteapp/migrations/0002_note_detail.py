# Generated by Django 3.1 on 2020-08-14 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noteapp.note')),
            ],
        ),
    ]
