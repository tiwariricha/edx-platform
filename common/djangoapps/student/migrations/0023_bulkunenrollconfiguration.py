# Generated by Django 1.11.24 on 2019-09-19 19:51


import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0022_indexing_in_courseenrollment'),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkUnenrollConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateTimeField(auto_now_add=True, verbose_name='Change date')),
                ('enabled', models.BooleanField(default=False, verbose_name='Enabled')),
                ('csv_file', models.FileField(help_text='It expect that the data will be provided in a csv file format with                     first row being the header and columns will be as follows:                     user_id, username, email, course_id, is_verified, verification_date', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv'])])),
                ('changed_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Changed by')),
            ],
            options={
                'ordering': ('-change_date',),
                'abstract': False,
            },
        ),
    ]