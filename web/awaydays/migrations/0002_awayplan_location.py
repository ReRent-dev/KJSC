# Generated by Django 2.2.5 on 2019-10-14 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awaydays', '0001_create_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('address1', models.CharField(
                    max_length=128, verbose_name='Address line 1')),
                ('address2', models.CharField(blank=True, default='',
                                              max_length=128, verbose_name='Address line 2')),
                ('zip_code', models.CharField(
                    max_length=12, verbose_name='ZIP / Postal code')),
                ('city', models.CharField(max_length=64, verbose_name='City')),
                ('notes', models.TextField(max_length=4096, verbose_name='notes')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AwayPlan',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField(db_index=True,
                                                    help_text='The date on which your time away will start', verbose_name='trip start date')),
                ('end_date', models.DateTimeField(db_index=True,
                                                  help_text='The date on which you will return home', verbose_name='trip end date')),
                ('title', models.CharField(help_text='A title for this trip away',
                                           max_length=150, verbose_name='trip title')),
                ('certainty', models.PositiveIntegerField(choices=[(0, 'LOW'), (1, 'MEDIUM'), (
                    2, 'HIGH')], help_text="The certainty with which you'll actually go on your trip", verbose_name='trip certainty')),
                ('cancelled', models.BooleanField(db_index=True, default=False)),
                ('location', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='awaydays.Location')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
