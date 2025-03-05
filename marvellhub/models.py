from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    level = models.CharField(
    max_length=20, 
    choices=[
        ('elementary', 'Elementary'), 
        ('high_school', 'High School')
        ]
    )


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    
