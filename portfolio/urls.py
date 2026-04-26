from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Licenciaturas
    path('licenciaturas/', views.licenciaturas_list, name='licenciaturas_list'),
    path('licenciaturas/nova/', views.licenciatura_create, name='licenciatura_create'),
    path('licenciaturas/<int:pk>/editar/', views.licenciatura_edit, name='licenciatura_edit'),
    path('licenciaturas/<int:pk>/apagar/', views.licenciatura_delete, name='licenciatura_delete'),

    # Docentes
    path('docentes/', views.docentes_list, name='docentes_list'),
    path('docentes/novo/', views.docente_create, name='docente_create'),
    path('docentes/<int:pk>/editar/', views.docente_edit, name='docente_edit'),
    path('docentes/<int:pk>/apagar/', views.docente_delete, name='docente_delete'),

    # Unidades Curriculares
    path('ucs/', views.ucs_list, name='ucs_list'),
    path('ucs/nova/', views.uc_create, name='uc_create'),
    path('ucs/<int:pk>/editar/', views.uc_edit, name='uc_edit'),
    path('ucs/<int:pk>/apagar/', views.uc_delete, name='uc_delete'),

    # Projetos
    path('projetos/', views.projetos_list, name='projetos_list'),
    path('projetos/novo/', views.projeto_create, name='projeto_create'),
    path('projetos/<int:pk>/editar/', views.projeto_edit, name='projeto_edit'),
    path('projetos/<int:pk>/apagar/', views.projeto_delete, name='projeto_delete'),

    # Tecnologias
    path('tecnologias/', views.tecnologias_list, name='tecnologias_list'),
    path('tecnologias/nova/', views.tecnologia_create, name='tecnologia_create'),
    path('tecnologias/<int:pk>/editar/', views.tecnologia_edit, name='tecnologia_edit'),
    path('tecnologias/<int:pk>/apagar/', views.tecnologia_delete, name='tecnologia_delete'),

    # TFCs
    path('tfcs/', views.tfcs_list, name='tfcs_list'),
    path('tfcs/novo/', views.tfc_create, name='tfc_create'),
    path('tfcs/<int:pk>/editar/', views.tfc_edit, name='tfc_edit'),
    path('tfcs/<int:pk>/apagar/', views.tfc_delete, name='tfc_delete'),

    # Competências
    path('competencias/', views.competencias_list, name='competencias_list'),
    path('competencias/nova/', views.competencia_create, name='competencia_create'),
    path('competencias/<int:pk>/editar/', views.competencia_edit, name='competencia_edit'),
    path('competencias/<int:pk>/apagar/', views.competencia_delete, name='competencia_delete'),

    # Formações
    path('formacoes/', views.formacoes_list, name='formacoes_list'),
    path('formacoes/nova/', views.formacao_create, name='formacao_create'),
    path('formacoes/<int:pk>/editar/', views.formacao_edit, name='formacao_edit'),
    path('formacoes/<int:pk>/apagar/', views.formacao_delete, name='formacao_delete'),
]