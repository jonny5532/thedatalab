# Generated by Django 2.2.6 on 2019-11-04 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='description',
            field=models.CharField(blank=True, help_text='20 words max.', max_length=250),
        ),
        migrations.AddField(
            model_name='software',
            name='description',
            field=models.CharField(blank=True, help_text='20 words max.', max_length=250),
        ),
        migrations.AddField(
            model_name='tool',
            name='description',
            field=models.CharField(blank=True, help_text='20 words max.', max_length=250),
        ),
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.CharField(blank=True, editable=False, max_length=50),
        ),
    ]
