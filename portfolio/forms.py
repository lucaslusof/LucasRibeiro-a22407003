from django import forms
from .models import Licenciatura, Docente, UnidadeCurricular, Projeto, Tecnologia, TFC, Competencia, Formacao

class LicenciaturaForm(forms.ModelForm):
    class Meta:
        model = Licenciatura
        fields = ['nome', 'sigla', 'url_site', 'descricao', 'imagem']
        widgets = {'descricao': forms.Textarea(attrs={'rows': 3})}

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nome', 'email', 'url_lusofona', 'foto']

class UCForm(forms.ModelForm):
    class Meta:
        model = UnidadeCurricular
        fields = '__all__'
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
            'objetivos': forms.Textarea(attrs={'rows': 3}),
            'programa': forms.Textarea(attrs={'rows': 3}),
            'metodologia': forms.Textarea(attrs={'rows': 3}),
            'bibliografia': forms.Textarea(attrs={'rows': 3}),
            'avaliacao': forms.Textarea(attrs={'rows': 3}),
            'apresentacao': forms.Textarea(attrs={'rows': 3}),
            'docentes': forms.CheckboxSelectMultiple(),
        }

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'uc', 'descricao', 'conceitos_aplicados', 'imagem',
                  'video_demo', 'link_github', 'tecnologias', 'competencias']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
            'conceitos_aplicados': forms.Textarea(attrs={'rows': 3}),
            'tecnologias': forms.CheckboxSelectMultiple(),
            'competencias': forms.CheckboxSelectMultiple(),
        }

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = ['nome', 'descricao', 'logo', 'url_site', 'nivel_interesse']
        widgets = {'descricao': forms.Textarea(attrs={'rows': 3})}

class TFCForm(forms.ModelForm):
    class Meta:
        model = TFC
        fields = ['titulo', 'resumo', 'ano', 'link_documento', 'destaque', 'tecnologias']
        widgets = {
            'resumo': forms.Textarea(attrs={'rows': 3}),
            'tecnologias': forms.CheckboxSelectMultiple(),
        }

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nome', 'descricao', 'nivel', 'tecnologias']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
            'tecnologias': forms.CheckboxSelectMultiple(),
        }

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = ['instituicao', 'descricao', 'data_inicio', 'data_fim', 'certificado', 'competencias_adquiridas']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
            'competencias_adquiridas': forms.CheckboxSelectMultiple(),
        }