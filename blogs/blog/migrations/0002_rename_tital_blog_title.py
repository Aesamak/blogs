# Generated by Django 5.1.4 on 2025-02-26 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='tital',
            new_name='title',
        ),
    ]
