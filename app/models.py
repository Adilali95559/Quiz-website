from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    desc=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.name

class QuizCategory(models.Model):

    tittle=models.CharField(max_length=100)
    detail=models.TextField()
    #image=models.ImageField(upload_to='/static/img')
    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.tittle

class QuizQuestion(models.Model):

    category=models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    question=models.TextField()
    opt_1=models.CharField(max_length=200)
    opt_2=models.CharField(max_length=200)
    opt_3=models.CharField(max_length=200)
    opt_4=models.CharField(max_length=200)
    level=models.CharField(max_length=100)
    time_limit=models.IntegerField()
    right_opt=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Question'

    def __str__(self):
        return self.question


class UserSubmittedAnswer(models.Model):
    question=models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    right_answer=models.CharField(max_length=200)

    class Meta():
        verbose_name_plural='User Submitted Answers'


class UserCategoryAttempts(models.Model):
    category=models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    attempt_time=models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural='User Attempts Category'


