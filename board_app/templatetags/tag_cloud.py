from django import template
from taggit. models import Tag

register = template.Library()


@register.inclusion_tag("board_app/components/tag_cloud.html")
def sidebar_tag_cloud():
    my_tag = Tag.objects.all()
    return {"tags": my_tag}
