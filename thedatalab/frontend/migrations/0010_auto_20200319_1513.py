# Generated by Django 2.2.6 on 2020-03-19 15:13

from django.db import migrations, models
import tagulous.models.fields
import tagulous.models.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_page_page_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'unique_together': {('slug',)},
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name='blog',
            name='type',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, blank=True, force_lowercase=True, help_text='Enter a comma-separated tag string', initial='blog-post, podcast', to='frontend.Types'),
        ),
        migrations.AddField(
            model_name='page',
            name='types',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, blank=True, force_lowercase=True, help_text='Enter a comma-separated tag string', initial='blog-post, podcast', to='frontend.Types'),
        ),
    ]
