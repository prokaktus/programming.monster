from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock

from apps.base.wagtail.blocks import MarkDownBlock, CodeBlock


class ArticleIndexPage(Page):
    """
    This is root page for Wagtail site.

    You need to configure your content tree to represent this hierarchy.
    """

    template = 'articles/article_index.html'

    body = StreamField([
        ('markdown', MarkDownBlock())
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        articles = self.get_descendants()
        context['articles'] = articles
        return context


class ArticlePage(Page):
    template = 'articles/article.html'

    body = StreamField([
        ('text', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', blocks.RawHTMLBlock()),
        ('markdown', MarkDownBlock()),
        ('sourcecode', CodeBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class InfoPage(Page):
    body = StreamField([
        ('text', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', blocks.RawHTMLBlock()),
        ('markdown', MarkDownBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
