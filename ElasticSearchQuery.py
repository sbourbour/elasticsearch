import requests
import json

def getData(searchTerm):
    url = "http://localhost:9200/books/_search?q=" + searchTerm    
    data = requests.get(url)        
    return data.json()


searchTerm = input('Please enter search term:')
responseContent = getData(searchTerm)

for entry in responseContent['hits']['hits']:    
    print(entry['_source'])
    print()