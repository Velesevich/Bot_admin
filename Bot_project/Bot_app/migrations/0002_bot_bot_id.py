# Generated by Django 4.0.6 on 2022-07-18 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bot_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='bot_id',
            field=models.CharField(default='1', max_length=20),
            preserve_default=False,
        ),
    ]