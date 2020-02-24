# Generated by Django 2.2.7 on 2020-02-23 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.CharField(default=None, max_length=100)),
                ('add_alias', models.CharField(default=None, max_length=50)),
                ('add_id', models.IntegerField(default=0)),
                ('fname', models.CharField(default=None, max_length=50)),
                ('lname', models.CharField(default=None, max_length=50)),
                ('email', models.CharField(default=None, max_length=50)),
                ('phone', models.IntegerField(default=0)),
                ('Address', models.CharField(max_length=5000)),
                ('courses', models.CharField(default=None, max_length=50)),
                ('tot_fees', models.CharField(max_length=50)),
                ('pay_fees', models.CharField(max_length=50)),
                ('one_install_date', models.CharField(blank=True, default=None, max_length=50)),
                ('one_install_fees', models.CharField(blank=True, default=None, max_length=50)),
                ('status', models.CharField(blank=True, default=None, max_length=50)),
                ('two_install_date1', models.CharField(blank=True, default=None, max_length=50)),
                ('two_install_fees1', models.CharField(blank=True, default=None, max_length=50)),
                ('two_install_date2', models.CharField(blank=True, default=None, max_length=50)),
                ('two_install_fees2', models.CharField(blank=True, default=None, max_length=50)),
                ('three_install_date1', models.CharField(blank=True, default=None, max_length=50)),
                ('three_install_fees1', models.CharField(blank=True, default=None, max_length=50)),
                ('three_install_date2', models.CharField(blank=True, default=None, max_length=50)),
                ('three_install_fees2', models.CharField(blank=True, default=None, max_length=50)),
                ('three_install_date3', models.CharField(blank=True, default=None, max_length=50)),
                ('three_install_fees3', models.CharField(blank=True, default=None, max_length=50)),
                ('status1', models.CharField(blank=True, default=None, max_length=50)),
                ('status2', models.CharField(blank=True, default=None, max_length=50)),
                ('status3', models.CharField(blank=True, default=None, max_length=50)),
                ('comments', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edate', models.CharField(default=None, max_length=100)),
                ('batchid', models.IntegerField(default=0)),
                ('batchalias', models.CharField(default=None, max_length=50)),
                ('trainer', models.CharField(max_length=50)),
                ('courses', models.CharField(default=None, max_length=50)),
                ('batch_time', models.CharField(default=None, max_length=50)),
                ('batch_days', models.CharField(default=None, max_length=50)),
                ('special_day', models.CharField(blank=True, default=None, max_length=50)),
                ('sname', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Enq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edate', models.CharField(default=None, max_length=100)),
                ('enqalias', models.CharField(default=None, max_length=50)),
                ('enqid', models.IntegerField(default=0)),
                ('fname', models.CharField(default=None, max_length=50)),
                ('lname', models.CharField(default=None, max_length=50)),
                ('email', models.CharField(default=None, max_length=50)),
                ('phone', models.IntegerField(default=0)),
                ('Address', models.CharField(max_length=5000)),
                ('courses', models.CharField(default=None, max_length=50)),
                ('enquiry', models.CharField(default=None, max_length=70)),
                ('reference_name', models.CharField(blank=True, default=None, max_length=100)),
                ('collagename', models.CharField(blank=True, default=None, max_length=100)),
                ('stream', models.CharField(blank=True, default=None, max_length=50)),
                ('year', models.CharField(blank=True, default=None, max_length=50)),
                ('company', models.CharField(blank=True, default=None, max_length=50)),
                ('designation', models.CharField(blank=True, default=None, max_length=50)),
                ('year_exper', models.CharField(blank=True, default=None, max_length=50)),
                ('Preferred_day', models.CharField(default=None, max_length=50)),
                ('weekday_date', models.CharField(blank=True, default=None, max_length=50)),
                ('weekdays_time', models.CharField(blank=True, default=None, max_length=50)),
                ('weekend_date', models.CharField(blank=True, default=None, max_length=50)),
                ('weekend_time', models.CharField(blank=True, default=None, max_length=50)),
                ('comments', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]
