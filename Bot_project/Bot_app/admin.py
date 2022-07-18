from django.contrib import admin
from .models import Bot, Products

# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug':('name',)}

admin.site.register(Bot)#,CategoryAdmin)
admin.site.register(Products)