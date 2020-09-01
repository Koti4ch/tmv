from django.db import models
from PIL import Image

# Create your models here.

class CarouselItem(models.Model):
    title = models.CharField("Заголовок", max_length=25, null=False, blank=False, default='ItemHeader')
    description = models.CharField("Описание", max_length=50, null=False, blank=False, default="Base description")
    image = models.ImageField(default='classic.jpg', null=False, upload_to='carouselfiles')
    delay = models.CharField("Зависание", max_length=3, default='400', null=False)
    active = models.BooleanField(default=True, null=False)

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'


    def __str__(self):
        return f'-- {self.title} --'

    def get_active_items():
        return CarouselItem.objects.filter(active=True)

    def save(self):
        super().save()
        with Image.open(self.image.path) as item:
            if item.height > 0 or item.width > 0:
                size = (600, 400)
                im = item.resize(size, Image.ANTIALIAS)
                im.save(self.image.path)