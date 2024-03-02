from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomUser)

admin.site.register(Post)
admin.site.register(Bulletin)
admin.site.register(Tag)
admin.site.register(Event)
admin.site.register(Comment)
