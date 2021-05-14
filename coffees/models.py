from django.db import models


# Create your models here.
from utils.models import TimestampModel


class Roast(models.TextChoices):
    # enum = value, display
    LIGHT = 'Light', '極淺度烘焙'
    CINNAMON = 'Cinnamon', '淺度烘焙'
    MEDIUM = 'Medium', '中度烘焙'
    HIGH = 'High', '中度微深烘焙'
    CITY = 'City', '中深度烘焙'
    FULL_CITY = 'Full-City', '微深度烘焙'
    FRENCH = 'French', '極深烘焙'
    ITALIAN = 'Italian', '極深度烘焙'


class OriginPlace(TimestampModel):
    name = models.CharField('名稱', max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '產地'
        verbose_name_plural = '產地'


class MainProcessing(TimestampModel):
    name = models.CharField('名稱', max_length=20, unique=True)

    def __str__(self):
        return self.name


class Tag(TimestampModel):
    name = models.CharField('名稱', max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '標籤'
        verbose_name_plural = '標籤'


class Coffee(TimestampModel):
    name = models.CharField('名稱', max_length=20, unique=True)
    description = models.TextField('描述')
    roast = models.CharField('烘培程度', max_length=10, choices=Roast.choices)
    price = models.PositiveIntegerField('價格')
    origin_place = models.ForeignKey(
        OriginPlace,
        on_delete=models.PROTECT,
        verbose_name='產地',
    )
    tags = models.ManyToManyField(Tag, verbose_name='標籤')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '咖啡'
        verbose_name_plural = '咖啡'
