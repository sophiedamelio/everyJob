# Generated by Django 3.2.9 on 2022-01-31 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20220131_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='job_title',
            field=models.ManyToManyField(to='main_app.JobTitle'),
        ),
    ]
