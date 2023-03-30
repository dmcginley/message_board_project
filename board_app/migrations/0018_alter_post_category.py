# Generated by Django 4.1.4 on 2023-03-28 12:57

import board_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0017_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Linux', 'Linux'), ('Ubuntu', 'Ubuntu'), ('Nextjs', 'Nextjs'), ('Tailwind CSS', 'Tailwind CSS'), ('Bulma', 'Bulma'), ('Java', 'Java')], default='general', max_length=100, verbose_name=board_app.models.Category),
        ),
    ]