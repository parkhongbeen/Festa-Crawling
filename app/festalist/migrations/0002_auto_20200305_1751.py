# Generated by Django 2.2.10 on 2020-03-05 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festalist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festalist',
            name='image',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='festalist',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]