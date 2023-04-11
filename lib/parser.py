import json

with open('data.json') as f:
    data = json.load(f)
    #Extract each item from the meta.view.columns list
    objects = json.items(f, 'meta.view.columns.item')
    columns = list(objects) #Convert generator to list

### headers = objects['headers']
### store = objects['store']
### injection_strings = objects['injection_strings']

### spoof_headers = headers['spoof_headers']
### tete_variation = headers['tete_variation']
### tete_headers = headers['tete_headers']
### tecl_headers = headers['tecl_headers']
### clte_headers = headers['clte_headers']
### METHOD_SQL = injection_strings['METHOD_SQL']

### valid = store['valid']
###invalid = store['invalid']

print(METHOD_SQL)
