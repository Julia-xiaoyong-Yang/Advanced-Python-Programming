#!/usr/bin/env python
# coding: utf-8

import requests

# Define the URL and headers
url = 'https://weatherapi-com.p.rapidapi.com/current.json?q=53.1%2C-0.13'
headers = {
    'x-rapidapi-host': 'weatherapi-com.p.rapidapi.com',
	'x-rapidapi-key': '5f58ef7abamsh44ba0a154d8c262p1109fajsn565594e0714b'
}

# Make the GET request
response = requests.get(url, headers=headers)

# Print the response status and JSON data
print(response.status_code)
print(response.json())
