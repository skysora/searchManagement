# Generated by Django 3.0.3 on 2020-03-15 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200315_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='box_type',
            field=models.CharField(choices=[('cuted off', 'cuted off'), ('packed', 'packed'), ('stocked out', 'stocked out')], max_length=255),
        ),
    ]
