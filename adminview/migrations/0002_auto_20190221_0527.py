# Generated by Django 2.1.7 on 2019-02-21 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='scourse',
            field=models.CharField(max_length=30),
        ),
    ]
