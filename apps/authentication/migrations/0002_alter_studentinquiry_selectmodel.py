# Generated by Django 3.2.6 on 2022-03-11 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinquiry',
            name='selectmodel',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
