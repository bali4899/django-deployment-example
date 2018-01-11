from django import relative_url_templates

register=temlate.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts oot all values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
