from django.conf import settings
from django.db import models
from django.utils import timezone

class QuizModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)
    question_title = models.CharField(max_length=14, unique=False, blank=False, null=False)
    question_id = models.IntegerField(unique=False, blank=False, null=False)
    question = models.TextField(blank=True, null=True)
    answer_num = models.IntegerField(blank=False, null=False)
    answer = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now, blank=False, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.question_title