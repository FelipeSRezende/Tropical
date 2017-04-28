from django.template import Library

register = Library()

@register.inclusion_tag('includes/paginador.html')
def paginacao(request,paginator,pagina_atual):

    context = {
        'paginator' : paginator,
        'request' : request,
        'page_obj' : pagina_atual
    }

    getvars = request.GET.copy()

    if  'page' in getvars:
        del getvars['page']

    if len(getvars) > 0:
        context['getvars'] = '&{0}'.format(getvars.urlencode())
    else:
        context['getvars'] = ''

    return context