from django.db import models

class Question(models.Model):
  subject = models.CharField(max_length=200)
  content = models.TextField()
  pub_date = models.DateTimeField()

class Answer(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  content = models.TextField()
  create_date = models.DateTimeField()

#polls_favorite
class Favorite(models.Model):
  answer = models.ForeignKey(
    Answer, on_delete=models.CASCADE)
    # 255.255.255.255
  ip = models.CharField(max_length=15)
  create_date = models.DateTimeField()
