# Generated by Django 4.0.6 on 2022-09-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Phone', '0024_remove_phone_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]