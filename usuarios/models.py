from django.db import models

class Aluno(models.Model):
    nome = models.CharField("Nome completo", max_length=100)
    matricula = models.CharField("Matrícula", max_length=20, unique=True)
    data_nascimento = models.DateField("Data de nascimento")
    turma = models.CharField("Turma", max_length=50)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"

class Professor(models.Model):
    nome = models.CharField("Nome completo", max_length=100)
    disciplina = models.CharField("Disciplina", max_length=100)
    email = models.EmailField("E-mail", unique=True)

    def __str__(self):
        return self.nome

class Gestor(models.Model):
    nome = models.CharField("Nome completo", max_length=100)
    cargo = models.CharField("Cargo", max_length=100)
    email = models.EmailField("E-mail", unique=True)

    def __str__(self):
        return f"{self.nome} - {self.cargo}"