from django.urls import path
from . import views
from . import csv_views

urlpatterns = [
    path('', views.index, name='index'),
    path('questions_list/', views.questions_list, name='questions_list'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('question/new/', views.question_new, name='question_new'),
    path('question/<int:pk>/edit/', views.question_edit, name='question_edit'),
    path('question/<int:pk>/delete/', views.question_delete, name='question_delete'),
    path('answers_list/', views.answers_list, name='answers_list'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('csv_make/<int:pk>/', csv_views.csv_make, name='csv_make'),
    path('question/<int:pk>/csv_read/', csv_views.csv_read, name='csv_read'),
    path('answer_analysis/<int:pk>/', csv_views.answer_analysis, name='answer_analysis'),
    #path('M5stack/', views.M5stack, name='M5stack'),
]