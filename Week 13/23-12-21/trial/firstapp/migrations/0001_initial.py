# Generated by Django 4.0 on 2021-12-23 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('did', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'StudentDetails',
                'verbose_name_plural': 'StudentDetailss',
            },
        ),
    ]
