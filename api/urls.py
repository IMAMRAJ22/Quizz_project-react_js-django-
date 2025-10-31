from django.urls import path, include
from .views import LoginViewSet, CourseViewSet, QuizViewSet, QuizOptViewSet, ResultViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('login', LoginViewSet)
router.register('course',CourseViewSet)
router.register('quiz',QuizViewSet)
router.register('quiz_options',QuizOptViewSet)
router.register('result', ResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
