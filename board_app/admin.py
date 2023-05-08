from django.contrib import admin
from .models import Post, Comment, Category
# from .models import Post
# from .models import QuillPost

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}  # new


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author')


@admin.register(Category)
class CommentCategory(admin.ModelAdmin):
    pass
    # list_display = ('category',)

    # @admin.register(Category)
    # class CategoryAdmin(admin.ModelAdmin):
    #     list_display = ('name',)

    # @admin.register(QuillPost)
    # class QuillPostAdmin(admin.ModelAdmin):
    #     pass
