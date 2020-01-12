from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock

from apps.base.wagtail.blocks import MarkDownBlock


class InfoPage(Page):
    body = StreamField([
        ('text', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', blocks.RawHTMLBlock()),
        ('markdown', MarkDownBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
