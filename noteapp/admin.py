from django.contrib import admin

# Register your models here.
from . models import Note,Note_Detail
admin.site.register(Note)
admin.site.register(Note_Detail)