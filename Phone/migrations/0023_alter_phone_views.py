# Generated by Django 4.0.6 on 2022-09-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Phone', '0022_phone_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
