# Generated by Django 3.0.3 on 2020-03-17 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20200317_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='id',
        ),
        migrations.AddField(
            model_name='sale',
            name='sale_id',
            field=models.CharField(default='0000001', max_length=255, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
