# Generated by Django 5.1.2 on 2024-11-18 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Manual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name=255)),
                ('publication_date', models.DateField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorials.language')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name=255)),
                ('manual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorials.manual')),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name=255)),
                ('content', models.TextField()),
                ('publication_date', models.DateField()),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorials.topic')),
            ],
        ),
    ]