from django import template

register = template.Library()


@register.filter
def time_duration(value1, value2):
    return (value1 - value2).days
