# Generated by Django 3.2.12 on 2022-10-24 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='ci',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
    ]
