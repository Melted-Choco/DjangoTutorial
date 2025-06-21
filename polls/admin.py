from django.contrib import admin

from .models import Choice, Question

# Customize the admin form
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 # by default, provide fields for 3 choices

class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    
    # Choice objects are edited on the Question admin page.
    inlines = [ChoiceInline]
    
    # Display a list of field names on the change list page
    list_display = ["question_text", "pub_date", "was_published_recently"]
    # Add a filter sidebar
    list_filter = ["pub_date"]
    # Add search capability
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)