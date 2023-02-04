from django import template
from users.models import region
register = template.Library()

@register.simple_tag
def get_region_from_id (region_id):
    region_var = region.objects.get(pk=region_id)
    return region_var
