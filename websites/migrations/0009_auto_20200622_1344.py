# Generated by Django 3.0.7 on 2020-06-22 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0008_auto_20200622_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='websites',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]