from django.contrib import admin
from django.contrib import admin
from .models import Article, Category, Comment


class ProfileAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    search_fields = ('user',)
    ordering = ['user', ]


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug', 'image', 'approved')
    list_filter = ('name', 'approved',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name', ]


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('category', 'title', 'slug', 'author', 'image', 'image_credit',
                    'body', 'date_published', 'status')
    list_filter = ('status', 'date_created', 'date_published', 'author',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'date_published'
    ordering = ['status', '-date_created', ]
    readonly_fields = ('views')

class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'comment', 'article', 'date_created', )
    list_filter = ('date_created', 'name',)
    search_fields = ('name', 'article', 'comment')
    date_hierarchy = 'date_created'
    ordering = ['-date_created', ]
    readonly_fields = ('name', 'email', 'comment', 'article', 'date_created', 'date_updated',)
