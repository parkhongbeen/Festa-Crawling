# Generated by Django 2.2.10 on 2020-03-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festalist', '0002_auto_20200305_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festalist',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
