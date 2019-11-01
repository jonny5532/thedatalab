# Generated by Django 2.2.6 on 2019-11-01 13:16

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('slug', models.SlugField(blank=True, editable=False)),
                ('position', models.CharField(blank=True, max_length=250)),
                ('biography', markdownx.models.MarkdownxField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('website_url', models.CharField(blank=True, max_length=150)),
                ('twitter_handle', models.CharField(blank=True, max_length=150)),
                ('is_alumni', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=False)),
                ('ordering', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['ordering'],
            },
        ),
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.CharField(blank=True, editable=False, max_length=100),
        ),
    ]
