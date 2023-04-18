from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.safestring import mark_safe 
from PIL import Image 
import os
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.
class User(AbstractUser):
    pass

class Application(models.Model):
    class APPLICATION_STATUSES(models.IntegerChoices):
        PENDING = 0
        ANSWERED = 1
        DONE = 2
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    country = CountryField(blank_label='(select country)')
    whatsapp = PhoneNumberField(blank=True)
    status = models.IntegerField(choices=APPLICATION_STATUSES.choices, default=0)
    
class GalleryImage(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='gallery')
    thumbnail =models.ImageField(upload_to='gallery', blank=True, null=True)
    def image_tag_admin(self): # new
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.thumbnail))   
    def save(self, *args, **kwargs):
        if not self.make_thumbnail():
            # set to a default thumbnail
            raise Exception('Could not create thumbnail - is the file type valid?')
        super(GalleryImage, self).save(*args, **kwargs)
    def make_thumbnail(self):
        THUMB_SIZE = (300, 300)
        thumb = Image.open(self.photo)
        thumb.thumbnail(THUMB_SIZE, Image.ANTIALIAS)
        thumb_name, thumb_extension = os.path.splitext(self.photo.name)             
        thumb_extension = thumb_extension.lower()
        thumb_filename = thumb_name + '_thumb' + thumb_extension
        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        elif thumb_extension == '.webp':
            FTYPE = 'WEBP'
        else:
            return False    # Unrecognized file type
        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        thumb.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)
        # set save=False, otherwise it will run in an infinite loop
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()
        return True

# Create your models here.
class Videos(models.Model):
    title = models.CharField(max_length=20, null=True)
    embed = models.CharField(max_length=1000)
    order = models.IntegerField(default=0)
    def preview(self): # new
        return mark_safe(self.embed)   
    