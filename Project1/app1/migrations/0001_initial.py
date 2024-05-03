# Generated by Django 5.0.4 on 2024-04-30 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=256)),
                ('Blood_group', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Disease', models.CharField(max_length=256)),
                ('Location', models.CharField(max_length=256)),
            ],
        ),
    ]
