from django.db import models

# Create your models here.
class Questionbank(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    question_type = models.CharField(max_length=100)

    class Meta:
        db_table = 'questionbank'