from django.db import models

class Login(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    uname=models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to='profile_img/', blank=True, null=True)
    
    def __str__(self):
        return self.email
    
class CourseCard(models.Model):
    name = models.CharField(max_length=50)
    course_img = models.ImageField(upload_to='images/', blank=True, null=True)
    des = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Quiz(models.Model):
    quiz_title = models.ForeignKey(CourseCard, related_name='quiz_title', on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    marks = models.IntegerField(default=1)
    
    def __str__(self):
        return self.question
    
class Quizoption(models.Model):
    quiz_ques = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_question')
    option = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.quiz_ques
    
class Result(models.Model):
    user_email = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='user_email')
    result = models.IntegerField(default=0)
    quiz_mark = models.IntegerField(default=0)
    course_title= models.ForeignKey(CourseCard, on_delete=models.CASCADE, related_name='course_title',  blank=True, null=True)
    def __str__(self):
        return self.user_email.email
