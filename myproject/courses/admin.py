from django.contrib import admin

# Register your models here.
from .models import Tee, TeeColor, Course, Round, Hole

admin.site.register(Tee)
admin.site.register(TeeColor)
admin.site.register(Course)
admin.site.register(Round)
admin.site.register(Hole)