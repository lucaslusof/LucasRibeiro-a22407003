from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Artigo, Comentario
from .forms import ArtigoForm, ComentarioForm

def artigos_list(request):
    artigos = Artigo.objects.all()
    return render(request, 'artigos/artigos_list.html', {'artigos': artigos})

def artigo_detail(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    comentarios = artigo.comentarios.all()
    form_comentario = ComentarioForm()

    if request.method == 'POST' and request.user.is_authenticated:
        form_comentario = ComentarioForm(request.POST)
        if form_comentario.is_valid():
            c = form_comentario.save(commit=False)
            c.artigo = artigo
            c.autor = request.user
            c.save()
            return redirect('artigo_detail', pk=pk)

    return render(request, 'artigos/artigo_detail.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form_comentario': form_comentario,
    })

@login_required
def artigo_create(request):
    if not request.user.groups.filter(name='autores').exists():
        return redirect('artigos_list')
    form = ArtigoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('artigos_list')
    return render(request, 'artigos/form.html', {'form': form, 'titulo': 'Novo Artigo'})

@login_required
def artigo_edit(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if artigo.autor != request.user:
        return redirect('artigos_list')
    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigo_detail', pk=pk)
    return render(request, 'artigos/form.html', {'form': form, 'titulo': 'Editar Artigo'})

@login_required
def artigo_like(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if request.user in artigo.likes.all():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)
    return redirect('artigo_detail', pk=pk)