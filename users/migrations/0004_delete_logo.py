# Generated by Django 3.2.2 on 2021-05-24 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_logo_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Logo',
        ),
    ]