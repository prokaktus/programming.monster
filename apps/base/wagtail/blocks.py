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
                'markdown.extensions.tables',
                'markdown.extensions.codehilite',
            ]
        )
        return mark_safe(f'<div class="markdown-block">{md}</div>')


class CodeBlock(MarkDownBlock):

    class Meta:
        icon = 'code'

    def render_basic(self, value, context=None):
        md = markdown(
            value,
            extensions=[
                'markdown.extensions.fenced_code',
                'markdown.extensions.codehilite',
            ]
        )
        return mark_safe(f'<div class="code-block">{md}</div>')
