from django.contrib import admin

from .models import Choice, Question

# Customize the admin form
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3 # by default, provide fields for 3 choices

class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline] # Choice objects are edited on the Question admin page.

admin.site.register(Question, QuestionAdmin)