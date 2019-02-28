# Generated by Django 2.1.7 on 2019-02-27 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='upload/images/')),
                ('content', models.TextField()),
                ('meta_title', models.CharField(max_length=60)),
                ('meta_description', models.CharField(max_length=160)),
                ('category', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogposts', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
    ]