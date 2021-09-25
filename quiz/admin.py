from django.contrib import admin
from.models import Question,Result,Course
# Register your models here.
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Result)