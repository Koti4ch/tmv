from django import template
from content.models import CarouselItem
from content.forms import ReviewForm


register = template.Library()

@register.simple_tag
def showAllActiveCarouselItems():
    return CarouselItem.get_active_items()

@register.simple_tag
def UserReviewForm():
    reviewform = ReviewForm()
    return reviewform