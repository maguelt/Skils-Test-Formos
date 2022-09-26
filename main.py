from utils import (
    safe_input,
    get_products,
    get_employees,
    get_sales
)

from actions import (
    register_sale,
    add_new_product,
    query_inventory_data,
    daily_report
)

def main():
    print("Welcome to Drink Store")
    print("""
Select your option

1. Register purchase
2. Add new product to stock
3. Show inventory 
4. Generate sales report
5. Exit
""")

    while True:
        action = safe_input('int_positive', 'Action: ')

        if action > 0 and action < 5:
            break

        print("Only press numbers within a range from 1 to 4")

    if action == 1:
        register_sale()
    elif action == 2:
        add_new_product()
    elif action == 3:
        query_inventory_data()
    elif action == 4:
        daily_report()
    else:
        print("Exit")

    print("Have a great day\n")

while True:
    main()

    again = input("Renter the menu? (y/n) ").strip()[0].lower()

    if (again == 'y'):
        continue
    else:
        print("Thank you for shopping with us\n")
        break
