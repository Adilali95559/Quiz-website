from django.contrib import admin
from app.models import Contact,QuizCategory,QuizQuestion,models,UserSubmittedAnswer,UserCategoryAttempts


# Register your models here.
admin.site.register(Contact)
admin.site.register(QuizCategory)
admin.site.register(QuizQuestion)
admin.site.register(UserSubmittedAnswer)
admin.site.register(UserCategoryAttempts)


class QuizQuestionAdmin(admin.ModelAdmin):
    list_display=[ 'question','level']
#admin.site.register(models.QuizQuestion,QuizQuestionAdmin)

class UserSubmittedAnswerAdmin(admin.ModelAdmin):
     list_display=['id' 'question','user' 'right_answer']
#admin.site.register(models.UserSubmittedAnswer,UserSubmittedAnswerAdmin)

class UserCategoryAttemptsAnswerAdmin(admin.ModelAdmin):
     list_display=['category','user','attempt_time']
