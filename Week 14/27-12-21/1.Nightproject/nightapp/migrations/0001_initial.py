# Generated by Django 4.0 on 2021-12-28 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_Details',
            fields=[
                ('usn', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=70)),
                ('location', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Personal_Details',
                'verbose_name_plural': 'Personal_Detailss',
            },
        ),
    ]
