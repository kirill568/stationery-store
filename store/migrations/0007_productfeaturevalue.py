# Generated by Django 3.0.5 on 2020-04-23 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200423_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeatureValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Feature', verbose_name='Характеристика')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product', verbose_name='Товар')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Value', verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Товар характеристика значение',
                'verbose_name_plural': 'Товары характеристики значения',
            },
        ),
    ]