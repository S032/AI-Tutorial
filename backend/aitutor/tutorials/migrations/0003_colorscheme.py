# Generated by Django 5.1.5 on 2025-01-18 11:38

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_alter_manual_name_alter_topic_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorScheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_color', models.CharField(default='#3776AB', max_length=7, validators=[django.core.validators.RegexValidator('^#(?:[0-9a-fA-F]{3}){1,2}$', 'Введите корректный HEX-цвет')])),
                ('secondary_color', models.CharField(default='#4B8BBE', max_length=7, validators=[django.core.validators.RegexValidator('^#(?:[0-9a-fA-F]{3}){1,2}$', 'Введите корректный HEX-цвет')])),
                ('background_color', models.CharField(default='#F0F4F8', max_length=7, validators=[django.core.validators.RegexValidator('^#(?:[0-9a-fA-F]{3}){1,2}$', 'Введите корректный HEX-цвет')])),
                ('text_color', models.CharField(default='#333333', max_length=7, validators=[django.core.validators.RegexValidator('^#(?:[0-9a-fA-F]{3}){1,2}$', 'Введите корректный HEX-цвет')])),
                ('accent_color', models.CharField(default='#FFD43B', max_length=7, validators=[django.core.validators.RegexValidator('^#(?:[0-9a-fA-F]{3}){1,2}$', 'Введите корректный HEX-цвет')])),
                ('language', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='color_scheme', to='tutorials.language')),
            ],
            options={
                'verbose_name': 'Цветовая схема',
                'verbose_name_plural': 'Цветовые схемы',
            },
        ),
    ]
