# Generated by Django 4.0.6 on 2022-08-26 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anamoly',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=1000)),
            ],
        ),
    ]
