# Generated by Django 2.2.10 on 2020-03-31 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('key', models.CharField(max_length=200)),
            ],
        ),
    ]