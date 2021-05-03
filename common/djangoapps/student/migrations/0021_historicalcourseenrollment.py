# Generated by Django 1.11.20 on 2019-04-25 20:18


import uuid

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_overviews', '0014_courseoverview_certificate_available_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0020_auto_20190227_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalCourseEnrollment',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, db_index=True, editable=False, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('mode', models.CharField(default='audit', max_length=100)),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('course', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='course_overviews.CourseOverview')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'db_table': 'student_courseenrollment_history',
                'verbose_name': 'historical course enrollment',
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]