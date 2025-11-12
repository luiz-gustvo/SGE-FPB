from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet, ProfessorViewSet, GestorViewSet

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'gestores', GestorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]