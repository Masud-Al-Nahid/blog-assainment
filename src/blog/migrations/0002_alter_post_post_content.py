# Generated by Django 4.1.7 on 2023-04-01 16:48

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]