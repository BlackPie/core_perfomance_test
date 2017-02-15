from django import template


register = template.Library()


@register.simple_tag
def is_allowed(user):
    if user.allowed:
        return 'Allowed'
    else:
        return 'Blocked'


@register.simple_tag
def bizzfuzz(user):
    if user.number % 3 != 0 and user.number % 5 != 0:
        return user.number
    else:
        result = ''
        if user.number % 3 == 0:
            result += 'Bizz'
        if user.number % 5 == 0:
            result += 'Fuzz'
        return result
