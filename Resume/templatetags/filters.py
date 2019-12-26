from django import template

register = template.Library()

@register.filter()
def changing(list: list, string_number):
    pass