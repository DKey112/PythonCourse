from django.contrib import admin
from just_app.models import Users,Category,Post
# Register your models here.

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','date_create','post')

    def post(self, obj):
        return obj.category_title.title