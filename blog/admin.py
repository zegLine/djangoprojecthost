from django.contrib import admin
from .models import Post, Event, Plane, PlaneVariation, PlaneImage

admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Plane)
admin.site.register(PlaneVariation)
admin.site.register(PlaneImage)