# Generated by Django 2.0.6 on 2018-06-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thingwithtopics',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]