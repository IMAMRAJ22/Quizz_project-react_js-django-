from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Login, CourseCard, Quiz, Quizoption, Result
from .serializers import LoginSerializer, CourseSerializer, QuizSerializer, QuizOptSerializer, ResultSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset = CourseCard.objects.all()
    serializer_class = CourseSerializer
    
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    
class QuizOptViewSet(viewsets.ModelViewSet):
    queryset = Quizoption.objects.all()
    serializer_class = QuizOptSerializer
    
class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    
    # specific user email get
    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get("user_email")
        course_id = self.request.query_params.get("course_title")
        if user_id:
            queryset = queryset.filter(user_email_id=user_id)
            queryset = queryset.filter(course_title_id = course_id)
        return queryset
    
    
    def create(self, request, *args, **kwargs):
        user_id = request.data.get("user_email")  # This is the Login FK
        score = request.data.get("result")
        quiz_mark = request.data.get("quiz_mark")
        course_id= request.data.get("course_title")

        if user_id is None or score is None:
            return Response({"error": "Missing fields"}, status=status.HTTP_400_BAD_REQUEST)

        # update_or_create will create if not exists, or update if exists
        result_obj, created = Result.objects.update_or_create(
            user_email_id=user_id,
            course_title_id = course_id,
            defaults={"result": score, "quiz_mark": quiz_mark}
        )

        serializer = self.get_serializer(result_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
