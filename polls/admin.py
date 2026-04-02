from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Registrem la Question amb els seus inlines
admin.site.register(Question, QuestionAdmin)

# IMPORTANT: Registrem Choice perquè tingui el seu propi menú i Selenium el trobi!
admin.site.register(Choice)
