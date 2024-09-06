# Generated by Django 5.1.1 on 2024-09-05 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=24)),
                ('first_name', models.CharField(max_length=24)),
                ('grade', models.IntegerField()),
                ('iep', models.BooleanField()),
                ('plan504', models.BooleanField()),
                ('eld', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=24)),
                ('subject', models.CharField(max_length=24)),
                ('credits', models.FloatField()),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.staffer')),
                ('students', models.ManyToManyField(to='main_app.student')),
            ],
        ),
    ]
