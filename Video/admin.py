from django.contrib import admin
from .models import NewVideo, VideoExplanation, MoreVideo


class NewVideoAdmin(admin.ModelAdmin):
    list_display = ('video_title', 'video_url')


class VideoExplanationAdmin(admin.ModelAdmin):
    list_display = ('video_subtitle', 'subtitle_explanation')


class MoreVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(NewVideo, NewVideoAdmin)
admin.site.register(VideoExplanation, VideoExplanationAdmin)
admin.site.register(MoreVideo, MoreVideoAdmin)

