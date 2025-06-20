from django import template
from django.template.defaultfilters import stringfilter
import markdown as md


register = template.Library()


@register.filter()  # 裝飾器語法
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])