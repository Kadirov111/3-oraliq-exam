from django.contrib import admin
from .models import Catalog
from posts.models import Post

class PostInline(admin.TabularInline):
    model = Post
    extra = 2
    fields = ('author',)

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    inlines = [PostInline]
