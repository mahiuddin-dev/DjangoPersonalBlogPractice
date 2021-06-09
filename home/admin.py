from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Home, Blogpost, Comment

# Register your models here.

# Home Admin
admin.site.register(Home)


# PostAdmin
class PostAdmin(SummernoteModelAdmin):
    list_display = [
        'postTitle',
        'thumPic',
    ]
    summernote_fields = ('description',)
    prepopulated_fields = {'slug': ['postTitle', ]}


admin.site.register(Blogpost, PostAdmin)


# CommentAdmin
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'body'
    ]


admin.site.register(Comment, CommentAdmin)
