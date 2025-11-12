from django.contrib import admin
from .models import Aluno, Professor, Gestor

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'turma')
    search_fields = ('nome', 'matricula', 'turma')
    list_filter = ('turma',)

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'disciplina', 'email')
    search_fields = ('nome', 'disciplina', 'email')

@admin.register(Gestor)
class GestorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'email')
    search_fields = ('nome', 'cargo', 'email')