from django.db import models


class TimestampModel(models.Model):
    create_at = models.DateTimeField('建立日期',auto_now_add=True)
    update_at = models.DateTimeField('修改日期',auto_now=True)

    class Meta:
        abstract = True