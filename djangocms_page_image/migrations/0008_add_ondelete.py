# Generated by Django 2.1.9 on 2019-08-30 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_page_image', '0001_squashed_0007_auto_20170914_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageextension',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='imageextension',
            name='preview_image',
            field=filer.fields.image.FilerImageField(blank=True, help_text='leave blank to use page image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preview_image_extensions', to=settings.FILER_IMAGE_MODEL, verbose_name='preview image'),
        ),
        migrations.AlterField(
            model_name='siblingpagepreviewplugin',
            name='style',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='style'),
        ),
    ]
