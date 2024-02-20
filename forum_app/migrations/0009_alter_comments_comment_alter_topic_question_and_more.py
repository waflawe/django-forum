# Generated by Django 4.2.2 on 2023-12-14 18:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0008_rename_header_topic_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=2048, null=True, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AlterField(
            model_name='topic',
            name='question',
            field=models.TextField(max_length=2048, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(16)]),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=100, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
    ]