from django.contrib import admin
from .models import Category,Post,Comment

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","create_by","display_categories","created_at"]
    list_filter = ["create_by","created_at"]
    search_fields = ["title","create_by__username","categories__name"]
    readonly_fields = ["created_at","last_modified"]

    def display_categories(self,obj):
        return ", ".join([category.name for category in obj.categories.all()])
    
    display_categories.short_description = "Categories"

    def save_model(self, request, obj, form, change):
        if not change:
            obj.create_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["author","post","created_at"]
    list_filter = ["created_at","post"]
    search_fields = ["author__username","post__title"]
    readonly_fields = ["created_at"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)
    