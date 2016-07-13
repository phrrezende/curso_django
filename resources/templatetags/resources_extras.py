from django import template

register = template.Library()

@register.filter(name="replace")
def replace(value,arg):
    return value.replace(arg, "")

#@register.filter(name="to_upper")
#@stringfilter
#def to_upper(value, arg):
#    return "%s -%s " % (value.upper(), arg)
