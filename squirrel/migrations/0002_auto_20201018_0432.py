# Generated by Django 3.1.2 on 2020-10-18 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squirrel',
            old_name='fur_color',
            new_name='furColor',
        ),
    ]
