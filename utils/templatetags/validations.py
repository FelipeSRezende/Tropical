from django.template import Library

register = Library()

@register.inclusion_tag('includes/validations.html')
def validations(errors):

    context = {
        'errors':errors
    }

    return context