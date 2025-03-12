from django.contrib import admin
from .models import blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "author"]
    search_fields = ["title", "author__username"]

admin.site.register(blog, BlogAdmin)
