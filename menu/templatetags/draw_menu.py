from django import template
from ..models import Subdivision, Employee
from .utils import (get_child_items,
                    get_querystring,
                    get_selected_item_id_list)

register = template.Library()


@register.inclusion_tag('tags/menu.html', takes_context=True)
def draw_menu(context, menu):
    try:
        items = Subdivision.objects.filter(is_active=True)
        items_values = items.values()
        primary_item = [item for item in items_values.filter(parent=None)]

        selected_item_id = int(context['request'].GET[menu])
        selected_item = items.get(id=selected_item_id)
        selected_item_id_list = get_selected_item_id_list(selected_item,
                                                          primary_item,
                                                          selected_item_id)

        for item in primary_item:
            if item['id'] in selected_item_id_list:
                item['child_items'] = get_child_items(items_values, item['id'],
                                                      selected_item_id_list)

        workers = Employee.objects.filter(
            subdivision__in=selected_item_id_list)

        result_dict = {'items': primary_item, 'workers': workers}

    except:
        result_dict = {
            'items': [
                item for item in
                Subdivision.objects.filter(is_active=True,
                                           parent=None).values()
            ],
            'workers': [
                worker for worker in
                Employee.objects.filter(subdivision=None).values()
            ]
        }

    result_dict['menu'] = menu
    result_dict['other_querystring'] = get_querystring(context, menu)

    return result_dict
