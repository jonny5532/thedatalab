# Generated by Django 2.2.6 on 2020-01-27 14:11

from django.db import migrations, models
import markdownx.models
import tagulous.models.fields

field_data = {}

def backup_fields(apps, schema_editor):
    print("BACKING UP")
    Project = apps.get_model("frontend", "Project")
    
    for p in Project.objects.all():
        field_data[p.id] = {
            'image':p.image, 
            'introduction':p.introduction,
            'overlay_text':p.overlay_text,
            'overlay_url':p.overlay_url
        }

    print(field_data)
    
def restore_fields(apps, schema_editor):
    print("RESTORING")
    Project = apps.get_model("frontend", "Project")
    
    for p in Project.objects.all():
        d = field_data[p.id]
        p.image = d['image']
        p.introduction = d['introduction']
        p.overlay_text = d['overlay_text']
        p.overlay_url = d['overlay_url']
        p.save()

class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_auto_20191216_1150'),
    ]

    operations = [
        migrations.RunPython(backup_fields, restore_fields),
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='introduction',
        ),
        migrations.RemoveField(
            model_name='project',
            name='overlay_text',
        ),
        migrations.RemoveField(
            model_name='project',
            name='overlay_url',
        ),
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='introduction',
            field=markdownx.models.MarkdownxField(blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='overlay_text',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='page',
            name='overlay_url',
            field=models.URLField(blank=True),
        ),
        migrations.RunPython(restore_fields, backup_fields),
        migrations.AlterField(
            model_name='page',
            name='topics',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, blank=True, force_lowercase=False, help_text='Enter a comma-separated tag string', initial='"Health/Changing Behaviour", "Health/Data Science", "Science/Conflicts of Interest", "Science/Trial Reporting", Health/OpenPrescribing, Health/Policy, Health/RCTs, Health/Research, Health/Variation, Science/Policy, Science/RCTs, Science/Retractions, Science/TrialsTrackers', related_name='pages', space_delimiter=False, to='frontend.TopicTags', tree=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='citation',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='thingwithtopics',
            name='topics',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, blank=True, force_lowercase=False, help_text='Enter a comma-separated tag string', initial='"Health/Changing Behaviour", "Health/Data Science", "Science/Conflicts of Interest", "Science/Trial Reporting", Health/OpenPrescribing, Health/Policy, Health/RCTs, Health/Research, Health/Variation, Science/Policy, Science/RCTs, Science/Retractions, Science/TrialsTrackers', related_name='things', space_delimiter=False, to='frontend.TopicTags', tree=True),
        ),
    ]
