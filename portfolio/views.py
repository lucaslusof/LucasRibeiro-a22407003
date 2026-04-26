from django.shortcuts import render, get_object_or_404, redirect
from .models import Licenciatura, Docente, UnidadeCurricular, Projeto, Tecnologia, TFC, Competencia, Formacao
from .forms import LicenciaturaForm, DocenteForm, UCForm, ProjetoForm, TecnologiaForm, TFCForm, CompetenciaForm, FormacaoForm
from escola.models import Curso, Aluno

def home(request):
    return render(request, 'portfolio/home.html', {
        'licenciaturas': Licenciatura.objects.all(),
        'ucs': UnidadeCurricular.objects.all(),
        'docentes': Docente.objects.all(),
        'projetos': Projeto.objects.all(),
        'tecnologias': Tecnologia.objects.all(),
        'competencias': Competencia.objects.all(),
        'formacoes': Formacao.objects.all(),
        'tfcs': TFC.objects.all(),
        'cursos': Curso.objects.all(),
        'alunos': Aluno.objects.all(),
    })

# ── Licenciaturas ──
def licenciaturas_list(request):
    return render(request, 'portfolio/licenciaturas_list.html', {'licenciaturas': Licenciatura.objects.all()})

def licenciatura_create(request):
    form = LicenciaturaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('licenciaturas_list')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Nova Licenciatura'})

def licenciatura_edit(request, pk):
    obj = get_object_or_404(Licenciatura, pk=pk)
    form = LicenciaturaForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('licenciaturas_list')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Licenciatura'})

def licenciatura_delete(request, pk):
    obj = get_object_or_404(Licenciatura, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('licenciaturas_list')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': obj, 'titulo': 'Apagar Licenciatura'})

# ── Docentes ──
def docentes_list(request):
    return render(request, 'portfolio/docentes_list.html', {'docentes': Docente.objects.all()})

def docente_create(request):
    form = DocenteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('docentes_list')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Novo Docente'})

def docente_edit(request, pk):
    obj = get_object_or_404(Docente, pk=pk)
    form = DocenteForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('docentes_list')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Docente'})

def docente_delete(request, pk):
    obj = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('docentes_list')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': obj, 'titulo': 'Apagar Docente'})

# ── Unidades Curriculares ──
def ucs_list(request):
    return render(request, 'portfolio/ucs_list.html', {'ucs': UnidadeCurricular.objects.all()})

def uc_create(request):
    form = UCForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('ucs_list')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Nova Unidade Curricular'})

def uc_edit(request, pk):
    obj = get_object_or_404(UnidadeCurricular, pk=pk)
    form = UCForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('ucs_list')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Unidade Curricular'})

def uc_delete(request, pk):
    obj = get_object_or_404(UnidadeCurricular, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('ucs_list')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': obj, 'titulo': 'Apagar UC'})

# ── Projetos ──
def projetos_list(request):
    return render(request, 'portfolio/projetos_list.html', {'projetos': Projeto.objects.all()})

def projeto_create(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('projetos_list')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Novo Projeto'})

def projeto_edit(request, pk):
    obj = get_object_or_404(Projeto, pk=pk)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('projetos_list')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Projeto'})

def projeto_delete(request, pk):
    obj = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('projetos_list')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': obj, 'titulo': 'Apagar Projeto'})

# ── Tecnologias ──
def tecnologias_list(request):
    return render(request, 'portfolio/tecnologias_list.html', {'tecnologias': Tecnologia.objects.all()})

def tecnologia_create(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('tecnologias_list')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Nova Tecnologia'})

def tecnologia_edit(request, pk):
    obj = get_object_or_404(Tecnologia, pk=pk)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('tecnologias_list')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Tecnologia'})

def tecnologia_delete(request, pk):
    obj = get_object_or_404(Tecnologia, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('tecnologias_list')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': obj, 'titulo': 'Apagar Tecnologia'})

# ── TFCs ──
def tfcs_list(request):
    return render(request, 'portfolio/tfcs_list.html', {'tfcs': TFC.objects.all()})

def tfc_create(request):
    form = TFCForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tfcs_list')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Novo TFC'})

def tfc_edit(request, pk):
    obj = get_object_or_404(TFC, pk=pk)
    form = TFCForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('tfcs_list')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar TFC'})

def tfc_delete(request, pk):
    obj = get_object_or_404(TFC, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('tfcs_list')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': obj, 'titulo': 'Apagar TFC'})

# ── Competências ──
def competencias_list(request):
    return render(request, 'portfolio/competencias_list.html', {'competencias': Competencia.objects.all()})

def competencia_create(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('competencias_list')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Nova Competência'})

def competencia_edit(request, pk):
    obj = get_object_or_404(Competencia, pk=pk)
    form = CompetenciaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('competencias_list')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Competência'})

def competencia_delete(request, pk):
    obj = get_object_or_404(Competencia, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('competencias_list')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': obj, 'titulo': 'Apagar Competência'})

# ── Formações ──
def formacoes_list(request):
    return render(request, 'portfolio/formacoes_list.html', {'formacoes': Formacao.objects.all()})

def formacao_create(request):
    form = FormacaoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('formacoes_list')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Nova Formação'})

def formacao_edit(request, pk):
    obj = get_object_or_404(Formacao, pk=pk)
    form = FormacaoForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('formacoes_list')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Formação'})

def formacao_delete(request, pk):
    obj = get_object_or_404(Formacao, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('formacoes_list')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': obj, 'titulo': 'Apagar Formação'})