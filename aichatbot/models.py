from django.db import models

# Create your models here.

# 챗봇 데이터 학습용 테이블

class ChatTrain(models.Model):
    id = models.AutoField(primary_key=True, null = False)   # 학습 데이터 id
    intent = models.CharField(max_length=45 )    # 의도명 의도가 없는 경우 null EX 실습장비 대여, 실습실 예약 등/
    ner = models.CharField(max_length=1024, null = True,default='')     # 개체명 개체가 없는 경우 null
    message = models.TextField(default='')        # 질문 텍스트
    answer = models.TextField(null = False)     # 답변 텍스트
    answer_image = models.CharField(max_length=2048, null = True, default='')    # 답변에 들어갈 이미지
