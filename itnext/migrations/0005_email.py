# Generated by Django 4.0.4 on 2022-06-04 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itnext', '0004_delete_brands'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]