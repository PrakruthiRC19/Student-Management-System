from django.db import models

# Create your models here.
COURSES = [
    ('JFS','Java Full Stack'),
    ('PFS','Python Full stack'),
    ('MERN','Mern Full Stack'),
    ('DS','Data Science'),
]

class Student(models.Model):
    name = models.CharField(max_length=150)
    roll_no = models.IntegerField()
    marks = models.FloatField()
    course = models.CharField(choices=COURSES,max_length=120)
    address = models.TextField()

    def __str__(self):
        return self.name
