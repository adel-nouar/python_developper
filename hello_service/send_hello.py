import random
import requests


bonjour = 'Helloooooo'
good_morning = 'Good Morning'
hi = 'Hiiiii'

items = [bonjour, good_morning, hi]

# Make a random hello
hello = items[random.randrange(len(items))]


url = "http://127.0.0.1:8000"

response = requests.post(
    url=f'{url}/hello',
    params={
        'hello': hello
    }
)

print(f'Status code: {response.status_code}, hello: {hello}')
