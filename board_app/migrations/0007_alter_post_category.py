# Generated by Django 4.1.4 on 2023-04-05 17:43

import board_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0006_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Linux', 'Linux'), ('Bulma', 'Bulma'), ('Django', 'Django')], default='general', max_length=100, verbose_name=board_app.models.Category),
        ),
    ]