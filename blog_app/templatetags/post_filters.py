from django import template

register = template.Library()
@register.filter(name='post_status')
def post_status(value):
    if value:
        return "completed"
    else:
        return "pending"
