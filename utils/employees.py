from .other import dict_from_entries


def get_employees():

    keys = ('id', 'name')
    employees = []

    file = open('employees.csv')

    for line in file:
        values = line.split(',')
        employees.append({
            keys[0]: int(values[0]),
            keys[1]: values[1].rstrip(),
        })

    file.close()
    return employees
