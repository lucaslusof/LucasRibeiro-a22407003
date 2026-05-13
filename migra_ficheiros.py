"""
migra_ficheiros.py
Coloca este ficheiro na raiz do projecto e corre:
    python manage.py shell
    >>> import migra_ficheiros
"""
import os
from django.core.files import File

# ── Docentes ──
from portfolio.models import Docente
for obj in Docente.objects.all():
    if obj.foto and obj.foto.name:
        try:
            local_path = os.path.join('media', obj.foto.name)
            if os.path.exists(local_path):
                with open(local_path, 'rb') as f:
                    obj.foto.save(os.path.basename(local_path), File(f), save=True)
                print(f"Docente migrado: {obj}")
        except Exception as e:
            print(f"Erro em {obj}: {e}")

# ── Licenciaturas ──
from portfolio.models import Licenciatura
for obj in Licenciatura.objects.all():
    if obj.imagem and obj.imagem.name:
        try:
            local_path = os.path.join('media', obj.imagem.name)
            if os.path.exists(local_path):
                with open(local_path, 'rb') as f:
                    obj.imagem.save(os.path.basename(local_path), File(f), save=True)
                print(f"Licenciatura migrada: {obj}")
        except Exception as e:
            print(f"Erro em {obj}: {e}")

# ── Unidades Curriculares ──
from portfolio.models import UnidadeCurricular
for obj in UnidadeCurricular.objects.all():
    if obj.imagem and obj.imagem.name:
        try:
            local_path = os.path.join('media', obj.imagem.name)
            if os.path.exists(local_path):
                with open(local_path, 'rb') as f:
                    obj.imagem.save(os.path.basename(local_path), File(f), save=True)
                print(f"UC migrada: {obj}")
        except Exception as e:
            print(f"Erro em {obj}: {e}")

# ── Projetos ──
from portfolio.models import Projeto
for obj in Projeto.objects.all():
    if obj.imagem and obj.imagem.name:
        try:
            local_path = os.path.join('media', obj.imagem.name)
            if os.path.exists(local_path):
                with open(local_path, 'rb') as f:
                    obj.imagem.save(os.path.basename(local_path), File(f), save=True)
                print(f"Projeto migrado: {obj}")
        except Exception as e:
            print(f"Erro em {obj}: {e}")

# ── Tecnologias ──
from portfolio.models import Tecnologia
for obj in Tecnologia.objects.all():
    if obj.logo and obj.logo.name:
        try:
            local_path = os.path.join('media', obj.logo.name)
            if os.path.exists(local_path):
                with open(local_path, 'rb') as f:
                    obj.logo.save(os.path.basename(local_path), File(f), save=True)
                print(f"Tecnologia migrada: {obj}")
        except Exception as e:
            print(f"Erro em {obj}: {e}")

# ── Cursos (Escola) ──
from escola.models import Curso
for obj in Curso.objects.all():
    if obj.imagem and obj.imagem.name:
        try:
            local_path = os.path.join('media', obj.imagem.name)
            if os.path.exists(local_path):
                with open(local_path, 'rb') as f:
                    obj.imagem.save(os.path.basename(local_path), File(f), save=True)
                print(f"Curso migrado: {obj}")
        except Exception as e:
            print(f"Erro em {obj}: {e}")

# ── MakingOf ──
from portfolio.models import MakingOf
for obj in MakingOf.objects.all():
    if obj.foto_papel and obj.foto_papel.name:
        try:
            local_path = os.path.join('media', obj.foto_papel.name)
            if os.path.exists(local_path):
                with open(local_path, 'rb') as f:
                    obj.foto_papel.save(os.path.basename(local_path), File(f), save=True)
                print(f"MakingOf migrado: {obj}")
        except Exception as e:
            print(f"Erro em {obj}: {e}")

print("\n✓ Migração concluída!")