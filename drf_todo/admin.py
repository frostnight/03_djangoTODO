from django.contrib import admin

# Register your models here.
from drf_todo.models import Todo

admin.site.register(Todo)
