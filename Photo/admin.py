from django.contrib import admin

from Photo.models import ImageCard


class ImageCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')


admin.site.register(ImageCard, ImageCardAdmin)

