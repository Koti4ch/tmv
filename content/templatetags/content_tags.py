from django import template
from content.models import CarouselItem


register = template.Library()

@register.simple_tag
def showAllActiveCarouselItems():
    return CarouselItem.get_active_items()