# Generated by Django 4.1.4 on 2023-03-24 21:34

import board_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0016_alter_comment_content_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Ubuntu', 'Ubuntu'), ('Linux', 'Linux'), ('Nextjs', 'Nextjs')], default='general', max_length=100, verbose_name=board_app.models.Category),
        ),
    ]