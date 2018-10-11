from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    created = models.DateTimeField(_('date created'), auto_now_add=True)
    modified = models.DateTimeField(_('date modified'), auto_now=True)

    class Meta:
        abstract = True
