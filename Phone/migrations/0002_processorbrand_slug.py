# Generated by Django 4.0.6 on 2022-08-01 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Phone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='processorbrand',
            name='slug',
            field=models.SlugField(max_length=70, null=True),
        ),
    ]
