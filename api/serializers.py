from rest_framework import serializers
from .models import Login, CourseCard, Quiz, Quizoption, Result

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCard
        fields = '__all__'
        
class QuizOptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizoption
        fields = '__all__'
        
        
class QuizSerializer(serializers.ModelSerializer):
    quiz_question = QuizOptSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = '__all__'
        

class ResultSerializer(serializers.ModelSerializer):
    user_email_name = serializers.CharField(source='user_email.email', read_only=True)
    course_name = serializers.CharField(source='course_title.name', read_only=True)
    class Meta:
        model = Result
        fields = ['id', 'user_email', 'result', 'quiz_mark', 'course_title', 'user_email_name', 'course_name']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Result.objects.all(),
                fields=['course_title'],
                message = "Already attended...."
            )
        ]