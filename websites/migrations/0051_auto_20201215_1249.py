# Generated by Django 3.0.8 on 2020-12-15 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0050_auto_20201215_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='position',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='options',
            name='position',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='products',
            name='position',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]