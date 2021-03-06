# Generated by Django 3.2.6 on 2022-05-24 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_user_fullname'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
                ('lastupdate', models.CharField(blank=True, max_length=255, null=True)),
                ('courseduration', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='courselogo')),
                ('chapter', models.CharField(blank=True, max_length=255, null=True)),
                ('topic', models.CharField(blank=True, max_length=255, null=True)),
                ('screan', models.ImageField(blank=True, null=True, upload_to='coursescrean')),
                ('desc', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
