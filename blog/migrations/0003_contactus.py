# Generated by Django 3.2.2 on 2021-05-27 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_about_descript'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
    ]