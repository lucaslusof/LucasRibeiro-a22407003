from django.contrib import admin
from .models import Curso, Aluno

admin.site.register(Aluno)

class CursoAdmin(admin.ModelAdmin):
    filter_horizontal = ('alunos',)

admin.site.register(Curso, CursoAdmin)