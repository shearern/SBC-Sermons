from __future__ import unicode_literals

from django.db import models

class Speaker(models.Model):
    title = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Session(models.Model):
    title = models.CharField(max_length=30)

class SbcClass(models.Model):
    '''
    A class that the recording belongs to (i.e.: Family Legacy)
    '''
    title = models.CharField(max_length=30)

class Series(models.Model):
    title = models.CharField(max_length=30)

class CoverImage(models.Model):
    image = models.ImageField(upload_to='cover_images')

class Recording(models.Model):
    recorded_at = models.DateField()
    speakers = models.ManyToManyField(Speaker, blank=True)
    title = models.CharField(max_length=120)
    series = models.ForeignKey(Series, on_delete=models.PROTECT, blank=True)
    session = models.ForeignKey(Session, on_delete=models.PROTECT)
    cover_image = models.ForeignKey(CoverImage, on_delete=models.PROTECT, blank=True)
    sbc_class = models.ForeignKey(SbcClass, on_delete=models.PROTECT, blank=True)
    hidden = models.BooleanField(default=False)

