# Generated by Django 2.2.10 on 2020-03-12 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festalist', '0011_auto_20200312_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festalist',
            name='link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='festalist',
            name='tickets',
            field=models.TextField(blank=True),
        ),
    ]