from django.utils.safestring import mark_safe
from markdown import markdown
from wagtail.core import blocks


class MarkDownBlock(blocks.TextBlock):
    """A MarkDown block for Wagtail streamfields."""

    class Meta:
        icon = 'code'

    def render_basic(self, value, context=None):
        md = markdown(
            value,
            extensions=[
                'markdown.extensions.fenced_code',
                'markdown.extensions.tables'
            ]
        )
        return mark_safe('<div class="markdown-block">{}</div>'.format(md))
