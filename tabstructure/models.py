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
    subpage_title = models.CharField(max_length=255, blank=False, null=True)
    subpage_subtitle = RichTextField(features=['bold', 'italic'])

    content_panels = Page.content_panels + [
        FieldPanel('page_title'),
        FieldPanel('page_subtitle'),
        FieldPanel('subpage_title'),
        FieldPanel('subpage_subtitle'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        indexpages = super(MainIndexPage, self).get_context(request)
        iospages = IOS.objects.child_of(self).live()
        pythonpages = Python.objects.child_of(self).live()
        nodejspages = NodeJS.objects.child_of(self).live()
        rubypages = Ruby.objects.child_of(self).live()
        androidpages = Android.objects.child_of(self).live()
        reactpages = React.objects.child_of(self).live()
        context = {
            'indexpages': indexpages,
            'iospages': iospages,
            'pythonpages': pythonpages,
            'nodejspages': nodejspages,
            'rubypages': rubypages,
            'androidpages': androidpages,
            'reactpages': reactpages,
        }
        return context
    

    class Meta:
        verbose_name = "MainIndex Page"
        verbose_name_plural = "MainIndex Pages"

class IOS(Page):

    templates = "templates/tabstructure/ios_page.html"

    ios_title = models.CharField(max_length=255, blank=False, null=True)
    ios_content_detail = models.CharField(max_length=255, blank=False, null=True)
    ios_extra_detail = RichTextField(null=True, blank=True)
    content = StreamField(
        [
        ("raw_content", RawContentBlock())
        ],
        null=True, 
        blank = True
    )

    content_panels = Page.content_panels + [
        FieldPanel('ios_title'),
        FieldPanel('ios_content_detail'),
        FieldPanel('ios_extra_detail'),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = "IOS Page"
        verbose_name_plural = "IOS Pages"


class Python(Page):
    
    templates = "templates/tabstructure/python_page.html"

    python_title = models.CharField(max_length=255, blank=False, null=True)
    python_content_detail = models.CharField(max_length=255, blank=False, null=True)
    python_extra_detail = RichTextField(null=True, blank=True)
    content = StreamField(
        [
        ("raw_content", RawContentBlock())
        ],
        null=True, 
        blank = True
    )

    content_panels = Page.content_panels + [
        FieldPanel('python_title'),
        FieldPanel('python_content_detail'),
        FieldPanel('python_extra_detail'),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = "python Page"
        verbose_name_plural = "python Pages"


class NodeJS(Page):
    
    templates = "templates/tabstructure/nodejs_page.html"

    nodejs_title = models.CharField(max_length=255, blank=False, null=True)
    nodejs_content_detail = models.CharField(max_length=255, blank=False, null=True)
    nodejs_extra_detail = RichTextField(null=True, blank=True)
    content = StreamField(
        [
        ("raw_content", RawContentBlock())
        ],
        null=True, 
        blank = True
    )

    content_panels = Page.content_panels + [
        FieldPanel('nodejs_title'),
        FieldPanel('nodejs_content_detail'),
        FieldPanel('nodejs_extra_detail'),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = "NodeJS Page"
        verbose_name_plural = "NodeJS Pages"


class Ruby(Page):
    
    templates = "templates/tabstructure/ruby_page.html"

    ruby_title = models.CharField(max_length=255, blank=False, null=True)
    ruby_content_detail = models.CharField(max_length=255, blank=False, null=True)
    ruby_extra_detail = RichTextField(null=True, blank=True)
    content = StreamField(
        [
        ("raw_content", RawContentBlock())
        ],
        null=True, 
        blank = True
    )

    content_panels = Page.content_panels + [
        FieldPanel('ruby_title'),
        FieldPanel('ruby_content_detail'),
        FieldPanel('ruby_extra_detail'),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Ruby Page"
        verbose_name_plural = "Ruby Pages"


class Android(Page):
    
    templates = "templates/tabstructure/android_page.html"

    android_title = models.CharField(max_length=255, blank=False, null=True)
    android_content_detail = models.CharField(max_length=255, blank=False, null=True)
    android_extra_detail = RichTextField(null=True, blank=True)
    content = StreamField(
        [
        ("raw_content", RawContentBlock())
        ],
        null=True, 
        blank = True
    )

    content_panels = Page.content_panels + [
        FieldPanel('android_title'),
        FieldPanel('android_content_detail'),
        FieldPanel('android_extra_detail'),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Android Page"
        verbose_name_plural = "Android Pages"
    

class React(Page):
    
    templates = "templates/tabstructure/react_page.html"

    react_title = models.CharField(max_length=255, blank=False, null=True)
    react_content_detail = models.CharField(max_length=255, blank=False, null=True)
    react_extra_detail = RichTextField(null=True, blank=True)
    content = StreamField(
        [
        ("raw_content", RawContentBlock())
        ],
        null=True, 
        blank = True
    )

    content_panels = Page.content_panels + [
        FieldPanel('react_title'),
        FieldPanel('react_content_detail'),
        FieldPanel('react_extra_detail'),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = "React Page"
        verbose_name_plural = "React Pages"