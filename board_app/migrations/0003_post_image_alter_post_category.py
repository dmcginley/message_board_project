# Generated by Django 4.1.4 on 2023-04-02 19:07

import board_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0002_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='post_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Linux', 'Linux'), ('Bulma', 'Bulma')], default='general', max_length=100, verbose_name=board_app.models.Category),
        ),
    ]