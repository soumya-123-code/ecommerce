from django import template
from frontuser.models import Category

register= template.Library()

@register.inclusion_tag(
	'frontuser/categorytag.html')
def category_snippets(**kwargs):
	categories = Category.objects.filter(**kwargs)
	return {
	     'categories': categories,


	}