from django.contrib import admin
from .models import Post
#customizing admin 
class PostMOdel(admin.ModelAdmin):
    list_display = ['title','content','date_created']
    search_fields = ['tile','date_created']



# Register your models here.
admin.site.register(Post,PostMOdel)
