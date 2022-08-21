# Generated by Django 4.0.6 on 2022-08-16 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Phone', '0014_phone_old_price_phone_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonebrand',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='phone_brand', to='Phone.phonebrand'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='processor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='phone_processor', to='Phone.processor'),
        ),
    ]