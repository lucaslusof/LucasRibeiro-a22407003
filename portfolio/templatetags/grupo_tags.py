from django import template

register = template.Library()

@register.filter
def no_grupo(user, grupo_nome):
    return user.groups.filter(name=grupo_nome).exists()