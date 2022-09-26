from utils import (
    get_products,
    select_by_id_or_name,
    safe_input,
    update_products
)

def add_new_product():
    print("--- Register product arrival ---\n")
    print("Input product\n")

    menu = get_products()

    for thing in menu:
        print(thing['name'], thing['id'])

    choosen_product = select_by_id_or_name(menu, 'product')

    arrival_quantity = safe_input('int_positive', 'New quantity:')

    choosen_product['quantity'] += arrival_quantity

    print('You\'ve registered %s item(s) of %s' %
          (arrival_quantity, choosen_product['name']))
    print(' %s left in stock' % choosen_product['quantity'])
    update_products(menu)
