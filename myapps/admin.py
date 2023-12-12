from django.contrib import admin
from .models import Home, About

# Register your models here.
# class AboutAdmin(admin.ModelAdmin):
#     list_display = ("name", "keterangan",)

# class HomeAdmin(admin.ModelAdmin):
#     list_display = ("name", "keterangan")

# class BlogAdmin(admin.ModelAdmin):
#     list_display = ("name", "keterangan",)
       
# admin.site.register(About, AboutAdmin)
# admin.site.register(Home, HomeAdmin)
# admin.site.register(Blog, BlogAdmin)

class ProdukAdmin(admin.ModelAdmin):
    list_display = ("name", "keterangan")

admin.site.register(Home, ProdukAdmin)
admin.site.register(About)