# Generated by Django 3.2.8 on 2021-11-09 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]