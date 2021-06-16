from django import template
from proshop.models import Order

register = template.Library()


@register.filter(name="cart_item_count")
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0

register.filter('cart_item_count', cart_item_count)
