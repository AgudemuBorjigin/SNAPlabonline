# Generated by Django 3.0.7 on 2020-06-11 04:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jspsych.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jstask',
            fields=[
                ('name', models.CharField(help_text='Short codename for task (no spaces)', max_length=24, primary_key=True, serialize=False, verbose_name='Name')),
                ('displayname', models.CharField(default='', help_text='Experimenter/Subject-friendly title or name for the task', max_length=80, verbose_name='Display Name')),
                ('descr', models.CharField(default='', help_text='Please provide a one sentence description', max_length=255, verbose_name='Short description')),
                ('icon', models.ImageField(help_text='Upload an image that will appear as an icon for this task', upload_to='taskicons/')),
                ('trialinfo', models.TextField(help_text='Paste the contents of JSON file with task information', validators=[jspsych.validators.taskjson_validate], verbose_name='Trial Info')),
                ('tasktype', models.SmallIntegerField(choices=[(1, 'constant-fixed'), (2, 'constant-randomized')], null=True)),
                ('task_url', models.CharField(default='q1pb1Mtz3t_nUSA7ma2rnP-XkhtpxRfU1Hu1aF1jl4A', max_length=32, unique=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('experimenter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SingleTrialResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jspsych.Jstask')),
            ],
        ),
        migrations.CreateModel(
            name='OneShotResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jspsych.Jstask')),
            ],
        ),
    ]