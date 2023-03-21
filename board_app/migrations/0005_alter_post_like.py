# Generated by Django 4.1.4 on 2023-03-15 16:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board_app', '0004_alter_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
