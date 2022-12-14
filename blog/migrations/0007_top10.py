# Generated by Django 4.0.6 on 2022-08-26 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Phone', '0015_phonebrand_published_alter_phone_brand_and_more'),
        ('blog', '0006_alter_blog_publish_date_alter_blog_update_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Top10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='blog')),
                ('publish_date', models.DateField()),
                ('seo_title', models.CharField(blank=True, max_length=80, null=True)),
                ('seo_des', models.TextField(blank=True, max_length=170, null=True)),
                ('slug', models.SlugField(blank=True, max_length=170, unique=True)),
                ('phone1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone1', to='Phone.phone')),
                ('phone10', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone10', to='Phone.phone')),
                ('phone2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone2', to='Phone.phone')),
                ('phone3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone3', to='Phone.phone')),
                ('phone4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone4', to='Phone.phone')),
                ('phone5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone5', to='Phone.phone')),
                ('phone6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone6', to='Phone.phone')),
                ('phone7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone7', to='Phone.phone')),
                ('phone8', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone8', to='Phone.phone')),
                ('phone9', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone9', to='Phone.phone')),
            ],
            options={
                'ordering': ['publish_date'],
            },
        ),
    ]
