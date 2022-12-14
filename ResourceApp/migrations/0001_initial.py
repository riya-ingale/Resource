# Generated by Django 4.0.6 on 2022-08-02 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Institutes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('a_id', models.AutoField(primary_key=True, serialize=False)),
                ('lab', models.IntegerField()),
                ('available_units', models.IntegerField()),
                ('day', models.TextField()),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('approved', models.IntegerField(default=0)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Institutes.resources')),
            ],
        ),
    ]
