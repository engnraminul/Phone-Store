# Generated by Django 4.0.6 on 2022-08-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Phone', '0003_processor_alter_processorbrand_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='processor',
            name='slug',
            field=models.SlugField(blank=True, max_length=70, null=True, unique=True),
        ),
    ]