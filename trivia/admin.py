from django.contrib import admin
from .models import Question, Choice, Score

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Score)