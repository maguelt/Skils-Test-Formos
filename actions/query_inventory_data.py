from utils import (
    get_products,
    select_by_id_or_name,
    safe_input
)


def query_inventory_data():

    print("---Query inventory data---\n")
    print("Choose product\n")

    list_products = get_products()

    for products in list_products:
        print(products['name'], products['id'])

    this_product = select_by_id_or_name(list_products, 'product')

    print("Id:", this_product["id"])
    print("Price:", this_product["price"])
    print("Quantity in stock:", this_product["quantity"])
