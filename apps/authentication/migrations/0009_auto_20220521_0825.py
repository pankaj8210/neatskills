# Generated by Django 3.2.6 on 2022-05-21 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_user_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch_timing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batchname', models.CharField(blank=True, max_length=200, null=True)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(auto_now_add=True)),
                ('timings', models.TimeField(auto_now_add=True)),
                ('duration', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.CharField(blank=True, max_length=10, null=True)),
                ('updatedby', models.CharField(blank=True, max_length=20, null=True)),
                ('lastupdatedon', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chaptername', models.CharField(blank=True, max_length=200, null=True)),
                ('active', models.CharField(max_length=10, null=True)),
                ('updatedby', models.CharField(max_length=20, null=True)),
                ('lastupdatedon', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('courseduration', models.CharField(blank=True, max_length=200, null=True)),
                ('courselogo', models.FileField(upload_to='')),
                ('coursechapter', models.CharField(blank=True, max_length=200, null=True)),
                ('coursetopic', models.CharField(blank=True, max_length=200, null=True)),
                ('coursetopicscreen', models.FileField(blank=True, null=True, upload_to='')),
                ('courseprice', models.CharField(blank=True, max_length=200, null=True)),
                ('coursedescription', models.CharField(blank=True, max_length=200, null=True)),
                ('active', models.CharField(blank=True, max_length=10, null=True)),
                ('updatedby', models.CharField(blank=True, max_length=20, null=True)),
                ('lastupdatedon', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicname', models.CharField(blank=True, max_length=200, null=True)),
                ('active', models.CharField(max_length=10, null=True)),
                ('updatedby', models.CharField(max_length=20, null=True)),
                ('lastupdatedon', models.CharField(max_length=20, null=True)),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.chapter')),
                ('courses', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.courses')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
        migrations.CreateModel(
            name='Topics_screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenname', models.CharField(blank=True, max_length=200, null=True)),
                ('active', models.CharField(max_length=10, null=True)),
                ('updatedby', models.CharField(max_length=20, null=True)),
                ('lastupdatedon', models.CharField(max_length=20, null=True)),
                ('chapterid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.chapter')),
                ('courseid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.courses')),
                ('topicsid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.topics')),
            ],
        ),
        migrations.CreateModel(
            name='Course_schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_schedulename', models.CharField(blank=True, max_length=200, null=True)),
                ('duration', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.CharField(blank=True, max_length=10, null=True)),
                ('updatedby', models.CharField(blank=True, max_length=20, null=True)),
                ('lastupdatedon', models.CharField(blank=True, max_length=20, null=True)),
                ('batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.batch_timing')),
                ('scourse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.courses')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.courses'),
        ),
    ]
