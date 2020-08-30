from django.contrib import admin
from .models import CarouselItem
# Register your models here.

@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'active')
    list_filter = ('active',)

    class Meta:
        verbose_name = '123'
        verbose_name_plural = '123s'