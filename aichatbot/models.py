from django.db import models

# Create your models here.

# 챗봇 데이터 학습용 테이블

class ChatTrain(models.Model):
    id = models.AutoField(primary_key=True, null = False)
    intent = models.CharField(max_length=45)
    ner = models.CharField(max_length=1024)
    query = models.TextField(default='')
    answer = models.TextField(null = False)
    answer_image = models.CharField(max_length=2048)
