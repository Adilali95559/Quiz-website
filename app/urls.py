from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about', views.about ,name='about'),
    path('logout', views.logoutUser ,name='logout'),
    path('contact', views.contact ,name='contact'),
    path('quiz', views.quiz ,name='quiz'),
    path('home', views.home ,name='home'),
    path('register', views.register ,name='register'),
    path('category-question/<int:cat_id>', views.category_question ,name='category_question'),
    path('submit-answer/<int:cat_id>/<int:quest_id>', views.submit_answer ,name='submit_answer'),
    
]
