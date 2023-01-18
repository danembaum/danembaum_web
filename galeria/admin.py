from django.contrib import admin
from galeria.models import PixelArt

#changing properties of Django Admin
class listPixelArts(admin.ModelAdmin):
    list_display  = ("id", "name", "description")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("category", )

admin.site.register(PixelArt, listPixelArts)

