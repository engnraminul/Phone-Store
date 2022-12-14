# Generated by Django 4.0.6 on 2022-08-02 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Phone', '0004_processor_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='processor',
            options={'ordering': ['-released']},
        ),
        migrations.AddField(
            model_name='processor',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Processor_Brand', to='Phone.processorbrand'),
        ),
    ]
