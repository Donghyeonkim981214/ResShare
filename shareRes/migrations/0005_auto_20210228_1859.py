# Generated by Django 3.1.7 on 2021-02-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareRes', '0004_auto_20210228_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_link',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_phone',
            field=models.CharField(max_length=40),
        ),
    ]
