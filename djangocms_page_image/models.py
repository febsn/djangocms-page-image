from django.db import models
from django.conf import settings

from filer.fields.image import FilerImageField

from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

class ImageExtension(PageExtension):
    image = FilerImageField(verbose_name=_('image'), blank=True, null=True)
    teaser = models.TextField(verbose_name=_('teaser'), blank=True)
    show_preview = models.BooleanField(
        verbose_name=_('show preview?'),
        default=True
    )
    
    class Meta:
        verbose_name=_('page image and teaser')


extension_pool.register(ImageExtension)


class ChildPagePreviewPlugin(CMSPlugin):
    STYLE_CHOICES = getattr(
        settings,
        'DJANGOCMS_PAGE_IMAGE_CPP_STYLE_CHOICES',
        []
    )
    DEFAULT_STYLE = getattr(
        settings,
        'DJANGOCMS_PAGE_IMAGE_CPP_DEFAULT_STYLE',
        ''
    )
    style = models.CharField(
        _('style'),
        choices=STYLE_CHOICES,
        default=DEFAULT_STYLE,
        max_length=50,
        blank=True
    )
    
