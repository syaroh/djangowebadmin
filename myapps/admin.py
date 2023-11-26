from django.contrib import admin
from .models import About, Home, Blog

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

admin.site.register(About)
admin.site.register(Home)
admin.site.register(Blog)