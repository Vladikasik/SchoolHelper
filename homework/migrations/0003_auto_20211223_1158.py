# Generated by Django 3.1.13 on 2021-12-23 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_alter_homework_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
