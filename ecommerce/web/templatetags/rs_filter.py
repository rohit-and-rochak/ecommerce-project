from django import template

register = template.Library()


@register.filter(name="rs")
def rs(value):
    return "₹ " + str(value)
