from django import template

register = template.Library()

@register.filter
def media_filter(path):
    """
    Возвращает готовый URL до медиа-файла.
    """
    if not path:
        return '#'
    return f'/media/{path}'