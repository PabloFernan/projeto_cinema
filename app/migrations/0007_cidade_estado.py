# Generated by Django 5.1.5 on 2025-02-01 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_snaks_delete_snack'),
    ]

    operations = [
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.CharField(default='Estado --', max_length=100, unique=True),
        ),
    ]
