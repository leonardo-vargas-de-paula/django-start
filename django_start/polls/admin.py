from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','__str__', 'pub_date')
    
    search_fields = ['id']
admin.site.register(Question, QuestionAdmin)