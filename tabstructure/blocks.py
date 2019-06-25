from wagtail.core import blocks

class RawContentBlock(blocks.StructBlock):
    
    raw_content = blocks.RawHTMLBlock(required=True, max_length=1024, help_text="Raw HTML content")

    class Meta:
        template = "tabstructure/raw_content.html"
        icon = "edit",
        label = "Raw Content"
