from django.contrib import admin

from .models import *


class ImageInlineAdmin(admin.TabularInline):
    model = PostImage
    fields = ('image',)
    max_num = 5


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin,]
    list_filter = ['created_by', 'created_at']


admin.site.register(Board)
admin.site.register(Topic)
# admin.site.register(Post)
# admin.site.register(PostImage)
