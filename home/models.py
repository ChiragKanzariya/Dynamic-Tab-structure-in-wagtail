from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    """ Home Page Model """

    templates = "templates/home/home_page.html"
    max_count = 1

    banner_title = models.CharField(max_length=255, blank=False, null=True)
    banner_subtitle = RichTextField(features=['bold', 'italic'])


    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('banner_subtitle'),

    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

