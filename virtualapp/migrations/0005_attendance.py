# Generated by Django 3.2.5 on 2021-07-25 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualapp', '0004_registeredstudents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('attendanceID', models.AutoField(primary_key=True, serialize=False)),
                ('studentId', models.IntegerField(default=0)),
                ('percentage', models.IntegerField(default=0)),
                ('date', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'attendance',
            },
        ),
    ]
