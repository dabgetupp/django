# Generated by Django 3.2.6 on 2021-08-13 09:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tugas',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=225),
            preserve_default=False,
        ),
    ]