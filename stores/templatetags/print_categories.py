from django import template
register = template.Library()

@register.simple_tag
def print_categories (categories_list):
    categories_string = ''

    for category in categories_list:
        categories_string = categories_string + category.name + "، "
    
    categories_string = categories_string[:-2]
    return categories_string
