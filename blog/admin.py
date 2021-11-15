from django.contrib import admin

from blog.models import Author, Post, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display= ("title", "date","author")
    list_filter = ("author", "caption","date")


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)