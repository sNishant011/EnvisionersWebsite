from django.contrib import admin

from Home.models import ImageCard, About


class ImageCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')


class AboutAdmin(admin.ModelAdmin):
    list_display = ('aboutline', 'quote')


admin.site.register(ImageCard, ImageCardAdmin)
admin.site.register(About, AboutAdmin)

