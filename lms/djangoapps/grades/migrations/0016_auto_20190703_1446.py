# Generated by Django 1.11.21 on 2019-07-03 14:46


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0015_historicalpersistentsubsectiongradeoverride'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpersistentsubsectiongradeoverride',
            name='override_reason',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='historicalpersistentsubsectiongradeoverride',
            name='system',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='persistentsubsectiongradeoverride',
            name='override_reason',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='persistentsubsectiongradeoverride',
            name='system',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]