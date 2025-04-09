incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

# Your code here
def data_transformer(data_list):
    return list(map(lambda e : f"{e['name']} {e['last_name']}", data_list))


    """ return [f"{p['name']} {p['last_name']}" for p in list] """

print(data_transformer(incoming_ajax_data))

