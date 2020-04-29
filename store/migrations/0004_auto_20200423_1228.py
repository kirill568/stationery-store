# Generated by Django 3.0.5 on 2020-04-23 12:28

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_category_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='product',
            name='features',
            field=django.contrib.postgres.fields.jsonb.JSONField(default='null'),
            preserve_default=False,
        ),
    ]
