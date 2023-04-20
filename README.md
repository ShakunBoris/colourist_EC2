# Colourist & Director Portfolio 
## Distinctiveness and Complexity
The website is a professional portfolio, my first commercial job. This version is kinda short version of it, without using 2-3 docker containers (nginx, postgres and django) due to AWS amazon services give simple EC2 for free. Currently i use it  online with nginx, through gunicorn socket. It has  responsive design, customized admin panel, interactive gallery of photos, before-after slide bar, video import from VIMEO using Vimeo API (you can check it in admin panel, is "videoss"), so on and so forth. But you neen to set the .env file with your VIMEO TOKEN for vimeo and other data.
### HOW TO USE 
In case of http://3.125.8.5/ doent's work (where the website lives), you can do the following to start the project locally:
- install python
- create folder "colourist" and navigate into this folder
- run "python -m venv .venv" in the console
- git clone all the files from the project's folder so that manage.py is at the same root as .venv folder
- run 'pip install -r requirements.txt' to install all needed dependencies. In case something goes wrong you are unable to install "psycopg2==2.9.5" or it doesn't work install "psycopg2-binary==2.9.5" manually.
- run "python manage.py makemigrations"
- run "python manage.py migrate"
- run "python manage.py createsuperuser" and create one
- run "python manage.py collectstatic" (just in case)
- create .env file in the same folder where settings.py are. VIMEO_TOKEN is needed for admin panel: 
    * CSRF_TRUSTED_ORIGINS= 
    * ALLOWED_HOSTS= 
    * SECRET_KEY= 
    * DEBUG=True 
    * VIMEO_TOKEN=

I believe DEBUG is True and VIMEO_TOKEN is enaugh.
- finally run "python manage.py runserver" and you good to go

### Gallery
Using admin panel you can add your images to the gallery, you just need to upload it and set a name for it. Thumbnails will be created automatically. I use PIL to make thumbnails in the front/models.py 

class GalleryImage(models.Model)

### Contact
/front/models.py 

class Application(models.Model):

On the /contact page you can leave application for Site owner to contact you, there I use installed and imported importedCountryField, PhoneNumberField, custom class APPLICATION_STATUSES. So  info that users leaves must be valid.

Then you can see applications, and sort them by status in admin page. list_filter = ('status',)

### Director
You can go to admin panel and go to videoss. I modified django templates, so now there is a button "import". This button, uses vimeo API, populates 3-rd custom table of the app with 'embed' links of videos from the Site owner vimeo page. 

**Don't forget to click 'save' button' down below the page afte any changes**

you can modify order of videos, and which will be shown on the /director page. 
* 0 - don't show
* any number - ascending order

# Additional
I use nanogallery2, wowjs and image-compare-viewer for gallery, element spawn effect and befor-after slidebar respectively.


