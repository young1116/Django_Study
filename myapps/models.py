from django.db import models

# Create your models here.

class Article(models.Model):  
    title = models.CharField(max_length =255 ) #최대 길이 설정
    content = models.TextField() #텍스트 필드 추가 
    created_at = models.DateTimeField(auto_now_add=True) #자동 생성 날짜/시간 추가

    def __str__(self):
        return self.title #객체를 문자열로 변환 하면 제목을 반환.    