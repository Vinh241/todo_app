from django.contrib import admin
from .models import TodoApp
class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(TodoApp,PostAdmin)