import requests
r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(r.json())