from django.contrib import admin
from .models import Licenciatura, Docente, UnidadeCurricular, Tecnologia, Projeto, TFC, Competencia, Formacao, MakingOf

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla']
    search_fields = ['nome', 'sigla']

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email']
    search_fields = ['nome', 'email']

@admin.register(UnidadeCurricular)
class UCAdmin(admin.ModelAdmin):
    list_display = ['sigla', 'nome', 'ano', 'semestre', 'ects']
    list_filter = ['ano', 'semestre']
    search_fields = ['nome', 'sigla']
    filter_horizontal = ['docentes']

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nivel_interesse']
    search_fields = ['nome']

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'uc']
    list_filter = ['uc']
    search_fields = ['titulo']
    filter_horizontal = ['tecnologias', 'competencias']

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'ano', 'destaque']
    list_filter = ['ano', 'destaque']
    search_fields = ['titulo']
    filter_horizontal = ['tecnologias']

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nivel']
    list_filter = ['nivel']
    search_fields = ['nome']
    filter_horizontal = ['tecnologias']

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'instituicao', 'data_inicio']
    list_filter = ['data_inicio']
    search_fields = ['descricao', 'instituicao']
    filter_horizontal = ['competencias_adquiridas']

@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'entidade_relacionada', 'criado_em']
    list_filter = ['entidade_relacionada']
    search_fields = ['titulo']