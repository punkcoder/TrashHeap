# Generated by Django 4.2.6 on 2023-10-27 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrashFile',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('filenames', models.TextField()),
                ('filepaths', models.TextField()),
                ('filetypes', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
