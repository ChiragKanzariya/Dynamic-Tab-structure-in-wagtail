from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from tabstructure.blocks import RawContentBlock


class MainIndexPage(Page):

    templates = "templates/tabstructure/main_index_page.html"

    page_title = models.CharField(max_length=255, blank=False, null=True)
    page_subtitle = RichTextField(features=['bold', 'italic'])

    content_panels = Page.content_panels + [
        FieldPanel('page_title'),
        FieldPanel('page_subtitle'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        indexpages = super(MainIndexPage, self).get_context(request)
        languagepages = Language.objects.child_of(self).live()
        context = {
            'indexpages': indexpages,
            'languagepages': languagepages,
        }
        return context
    

    class Meta:
        verbose_name = "MainIndex Page"
        verbose_name_plural = "MainIndex Pages"

class Language(Page):

    templates = "templates/tabstructure/language_page.html"

    language_title = models.CharField(max_length=255, blank=False, null=True)
    language_content_detail = models.CharField(max_length=255, blank=False, null=True)
    language_extra_detail = RichTextField(null=True, blank=True)
    content = StreamField(
        [
        ("raw_content", RawContentBlock())
        ],
        null=True, 
        blank = True
    )

    content_panels = Page.content_panels + [
        FieldPanel('language_title'),
        FieldPanel('language_content_detail'),
        FieldPanel('language_extra_detail'),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Language Page"
        verbose_name_plural = "Language Pages"

