# Generated by Django 4.1.4 on 2023-03-15 16:35

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0005_alter_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
    ]