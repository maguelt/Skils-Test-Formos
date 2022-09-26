from .other import dict_to_csv_line

keys = ('id', 'name', 'price', 'quantity')


def get_products():
    data = []
    file = open('products.csv')

    for line in file:
        spacing = line.split(',')
        product = {
            "id": int(spacing[0]),
            "name": spacing[1],
            "price": float(spacing[2]),
            "quantity": int(spacing[3])
        }
        data.append(product)

    file.close()
    return data

def update_products(product_list):
    file = open('products.csv', 'w')
    for p in product_list:
        line = dict_to_csv_line(p, keys)
        file.write(line)

    file.close()
