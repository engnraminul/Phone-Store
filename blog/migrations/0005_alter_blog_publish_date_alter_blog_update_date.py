# Generated by Django 4.0.6 on 2022-08-24 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_publish_date_alter_blog_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
