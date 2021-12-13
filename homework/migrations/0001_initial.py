# Generated by Django 3.1.4 on 2021-12-13 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('task_file', models.URLField()),
                ('priority', models.IntegerField(default=0)),
                ('date_given', models.DateTimeField(auto_now=True)),
                ('expiration_date', models.DateTimeField()),
                ('result_in_system', models.BooleanField(default=False)),
                ('link_to_result', models.URLField()),
                ('result_text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]