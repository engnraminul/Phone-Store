# Generated by Django 4.0.6 on 2022-08-05 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Phone', '0006_phonebrand_alter_processorbrand_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processor',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Processor_Brand', to='Phone.processorbrand'),
        ),
        migrations.AlterField(
            model_name='processor',
            name='seo_des',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Released', 'Released'), ('Upcoming', 'Upcoming'), ('Rumor', 'Rumor'), ('Draft', 'Draft')], max_length=20)),
                ('annoucement', models.DateField()),
                ('release', models.DateField()),
                ('network_type', models.CharField(max_length=100)),
                ('network_speed', models.CharField(max_length=100)),
                ('sim', models.CharField(max_length=50)),
                ('two_g', models.BooleanField(default=True)),
                ('two_g_band', models.CharField(max_length=100)),
                ('three_g', models.BooleanField(default=True)),
                ('three_g_band', models.CharField(max_length=100)),
                ('four_g', models.BooleanField(default=False)),
                ('four_g_band', models.CharField(max_length=100)),
                ('five_g', models.BooleanField(default=False)),
                ('five_g_band', models.CharField(max_length=100)),
                ('six_g', models.BooleanField(default=False)),
                ('six_g_band', models.CharField(max_length=100)),
                ('seven_g', models.BooleanField(default=True)),
                ('seven_g_band', models.CharField(max_length=100)),
                ('dimension', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=20)),
                ('front', models.CharField(max_length=50)),
                ('back', models.CharField(max_length=50)),
                ('frame', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=100)),
                ('body_feature', models.TextField()),
                ('display_type', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=20)),
                ('resulation', models.CharField(max_length=50)),
                ('ratio', models.CharField(max_length=20)),
                ('pixel_density', models.CharField(max_length=20)),
                ('refresh_rate', models.CharField(max_length=20)),
                ('protection', models.CharField(max_length=100)),
                ('display_features', models.CharField(max_length=100)),
                ('back_camera', models.TextField()),
                ('back_camera_features', models.CharField(max_length=150)),
                ('back_camera_video', models.CharField(max_length=150)),
                ('front_camera', models.TextField()),
                ('front_camera_features', models.CharField(max_length=150)),
                ('front_camera_video', models.CharField(max_length=150)),
                ('os', models.CharField(max_length=50)),
                ('os_version', models.CharField(max_length=50)),
                ('ui', models.CharField(max_length=50)),
                ('chipset', models.TextField()),
                ('ram', models.CharField(max_length=100)),
                ('storage', models.CharField(max_length=100)),
                ('memory_slot', models.BooleanField(default=False)),
                ('variant', models.CharField(max_length=50)),
                ('storage_type', models.CharField(max_length=50)),
                ('speaker', models.CharField(max_length=100)),
                ('audio_jack', models.BooleanField(default=False)),
                ('audio_features', models.CharField(max_length=100)),
                ('wifi', models.CharField(max_length=100)),
                ('hotspot', models.BooleanField(default=True)),
                ('nfc', models.BooleanField(default=False)),
                ('gps', models.BooleanField(default=True)),
                ('radio', models.BooleanField(default=True)),
                ('usb', models.CharField(max_length=100)),
                ('infrared_port', models.BooleanField(default=False)),
                ('fingureprint', models.CharField(max_length=100)),
                ('facelock', models.CharField(max_length=100)),
                ('sensor', models.CharField(max_length=200)),
                ('battery_type', models.CharField(max_length=100)),
                ('battery_capacity', models.CharField(max_length=50)),
                ('charging', models.CharField(max_length=100)),
                ('wireless_charging', models.CharField(max_length=100)),
                ('reverse_charging', models.CharField(max_length=100)),
                ('charging_features', models.TextField()),
                ('united_states', models.TextField()),
                ('europe', models.TextField()),
                ('india', models.TextField()),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Phone.phonebrand')),
                ('processor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Phone.processor')),
            ],
        ),
    ]
