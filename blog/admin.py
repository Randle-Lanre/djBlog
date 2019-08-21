from django.contrib import admin
from .models import Post

#used to register the db models where Post is the name of the class defined in models and 
#inherits from the models function of the models class
admin.site.register(Post)