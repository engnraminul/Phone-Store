# Generated by Django 4.0.6 on 2022-09-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_top10'),
    ]

    operations = [
        migrations.AddField(
            model_name='top10',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]