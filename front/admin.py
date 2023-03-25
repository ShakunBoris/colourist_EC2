from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Application, GalleryImage


class AppDisplay(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'country', 'whatsapp', 'status',]
    list_filter = ('status',)
    # filter_horizontal = ['status',]
class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "image_tag_admin", "photo"]

    
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Application, AppDisplay)
admin.site.register(GalleryImage, imageAdmin)


