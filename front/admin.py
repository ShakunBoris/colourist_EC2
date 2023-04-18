from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Application, GalleryImage, Videos
from django.shortcuts import redirect
from django.urls import path
import requests
import re
import environ
 
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


class AppDisplay(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'country', 'whatsapp', 'status',]
    list_filter = ('status',)
    # filter_horizontal = ['status',]
class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "image_tag_admin", "photo"]

class VideosDisplay(admin.ModelAdmin):
    actions = ["add_new"]
    list_display = ["order", "title", "preview"]
    list_display_links = ["title",]
    list_editable = ["order",]

    def add_new():
        pass

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [path("import/", self.admin_site.admin_view(self.video_import))]
        return my_urls + urls

    def video_import(self, request):
        user_id = "alvicolor"
        access_token = env('VIMEO_TOKEN')
        url = f"https://api.vimeo.com/users/{user_id}/videos"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
        response = requests.get(url, headers=headers)
        videos = response.json()["data"]
        lst = []
        for video in videos:
            video["embed"]["html"] = re.sub(
                '(?<=width=")\d+(?="\s)', "480", video["embed"]["html"]
            )
            video["embed"]["html"] = re.sub(
                '(?<=height=")\d+(?="\s)', "360", video["embed"]["html"]
            )
            lst.append((video['name'], video["embed"]["html"]))
            # tmp_obj = Test(title=video['name'], embed=video["embed"]["html"])
            # tmp_obj.save()
            obj, created = Videos.objects.get_or_create(title=video['name'])
            # If an object was created, set its fields
            if created:
                obj.embed = video["embed"]["html"]
                obj.save()
        context = dict(
            # Include common variables for rendering the admin template.
            self.admin_site.each_context(request),
            # Anything else you want in the context...
            # key=value,
            )
        return redirect("admin:front_videos_changelist")


# Register your models here.

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Application, AppDisplay)
admin.site.register(GalleryImage, imageAdmin)
admin.site.register(Videos, VideosDisplay)   


