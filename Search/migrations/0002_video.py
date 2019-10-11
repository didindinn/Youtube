# Generated by Django 2.2.6 on 2019-10-09 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(null=True)),
                ('video_url', models.URLField()),
                ('thumbnail', models.URLField()),
                ('channel_title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('video_duration', models.DurationField()),
                ('channel_url', models.URLField()),
            ],
        ),
    ]
