import json

data = [{'a': 1, 'b': 2, 'c':[1, 2, 3, 4]}]

data2 = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
print(data2)