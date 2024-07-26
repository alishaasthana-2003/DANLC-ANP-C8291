# Existing dictionary
my_dict = {
    'name': 'John Doe',
    'id': 123,
    'department': 'Sales'
}

updates = [
    ['Jane Smith', 456],
    ['Alice Johnson', 789]
]def update_dict_with_list(dictionary, update_list):
    for name, id in update_list:
        dictionary['name'] = name
        dictionary['id'] = id
update_dict_with_list(my_dict, updates)

print(my_dict)
