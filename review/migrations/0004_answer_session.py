# Generated by Django 3.1.2 on 2020-10-12 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='session',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
