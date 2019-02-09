from django import template
register = template.Library()

def cut(value, arg):
    """Removes all values of arg from the given string"""
    return str (value).replace(arg, '')

def jodo(value, arg):
    return str (value) + str (arg)

def lmbai(value, arg):
    return (str (value) + str (arg)).length()

register.filter('cut', cut)
register.filter('jodo', jodo)
register.filter('lmbai', lmbai)
register.filter('cut', cut)
