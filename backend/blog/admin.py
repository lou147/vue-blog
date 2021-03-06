from django.contrib import admin
from .models import Article, Tag, Comment, ViewInfo, FileManage


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'show_tags', 'create_time', 'update_time']
    search_fields = ['title', 'show_tags', 'create_time', 'update_time']

    def show_tags(self, obj):
        return ','.join([a.name for a in obj.tag.all()])


class CommentAdmin(admin.ModelAdmin):
    list_display = ['belong_to', 'parent', 'comment_user', 'create_time', 'user_ip']
    search_fields = ['belong_to', 'comment_user', 'create_time']


class ViewInfoAdmin(admin.ModelAdmin):
    list_display = ['view_ip', 'view_time']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ViewInfo, ViewInfoAdmin)
admin.site.register(FileManage)
