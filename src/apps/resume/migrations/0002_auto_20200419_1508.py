# Generated by Django 3.0.5 on 2020-04-19 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resumepage',
            old_name='block',
            new_name='preview',
        ),
    ]