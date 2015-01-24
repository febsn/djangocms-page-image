from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import ugettext_lazy as _

from .models import ChildPagePreviewPlugin


class CMSChildPagePreviewPlugin(CMSPluginBase):
    model = ChildPagePreviewPlugin
    
    name = _("Child Page Preview")
    render_template = "djangocms_page_image/plugins/child_page_preview.html"
    
    def render(self, context, instance, placeholder):
        request = context['request']
        if request.user.has_perm('cms.can_change'):
            context['subpages'] = request.current_page.children.all()
        else:
            context['subpages'] = request.current_page.children.published()
        return context

plugin_pool.register_plugin(CMSChildPagePreviewPlugin)

