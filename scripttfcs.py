import os
import json
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.conf import settings
from portfolio.models import TFC

ficheiro = os.path.join(settings.BASE_DIR, "data", "tfcs_2025.json")

if not os.path.isfile(ficheiro):
    print("JSON não encontrado!")
    quit()

with open(ficheiro, encoding="utf-8") as file:
    registos = json.load(file)

novos = 0

for reg in registos:
    nome_tfc = reg.get("titulo")

    if not nome_tfc:
        continue

    obj, criado = TFC.objects.get_or_create(
        titulo=nome_tfc,
        defaults={
            "resumo": reg.get("resumo", ""),
            "ano": reg.get("ano", 2025),
            "link_documento": reg.get("link_documento", ""),
            "destaque": False,
        },
    )

    if criado:
        novos += 1
        print(f"Adicionado: {nome_tfc}")
    else:
        print(f"Já existia: {nome_tfc}")

print(f"\nTotal inseridos: {novos}")