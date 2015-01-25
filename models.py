from django.db import models

from filer.fields.image import FilerImageField

from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

class ImageExtension(PageExtension):
    image = FilerImageField(verbose_name=_('image'), blank=True)
    teaser = models.TextField(verbose_name=_('teaser'), blank=True)
    
    class Meta:
        verbose_name=_('page image and teaser')
    
    def __unicode__(self):
        return self.image.label

extension_pool.register(ImageExtension)


class ChildPagePreviewPlugin(CMSPlugin):
    pass
