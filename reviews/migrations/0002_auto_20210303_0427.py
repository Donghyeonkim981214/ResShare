# Generated by Django 3.1.7 on 2021-03-02 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='restaruant',
            new_name='restaurant',
        ),
    ]
