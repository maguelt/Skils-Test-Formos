from utils import (
    safe_input,
    select_by_id_or_name,
    today,
    get_products,
    update_products,
    get_employees,
    get_sales,
    add_sale
)

def register_sale():
    sale = {
        "date": today()
    }

    print("--- Register sale ---\n")
    print("Who is selling?")

    employees = get_employees()
    for e in employees:
        print("- %s (%s)" % (e['name'], e['id']))
    print()

    employee = select_by_id_or_name(employees, 'employee')
    sale['employee_id'] = employee['id']

    print("Selected: %s (%s)\n" % (employee['name'], employee['id']))
    print("What product?")
    products = get_products()

    for p in products:
        print("- %s (%s) (%s left in stock)" %
              (p['name'], p['id'], p['quantity']))
    print()

    product = select_by_id_or_name(products, 'product')

    sale['product_id'] = product['id']

    print("Selected: %s (%s) (%s left in stock)\n" %
          (product['name'], product['id'], (product['quantity'])))

    quantity = 0
    while True:
        quantity = safe_input("int_positive", "How many items? ")
        if quantity > 0 and quantity <= product['quantity']:
            print("The order is valid")
            break
        else:
            print(
                "The order is invalid. Not enough stock")

    product['quantity'] -= quantity
    sale['num_products'] = quantity
    sale['total_price'] = quantity * product['price']

    print("\nTotal price: $%s + $%s tax" %
          (sale['total_price'], sale['total_price'] * 0.12))

    sale['id'] = len(get_sales())

    print("\nYour order's number is", sale['id'])

    update_products(products)
    add_sale(sale)
