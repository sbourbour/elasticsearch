import requests
import json
from elasticsearch import Elasticsearch 

def getData(searchTerm):
    url = "http://localhost:9200/books/_search?q=" + searchTerm    
    data = requests.get(url)        
    return data.json()


searchTerm = input('Please enter search term:')
responseContent = getData(searchTerm)

for entry in responseContent['hits']['hits']:    
    print(entry['_source'])
    print()
    
searchField = input('Please enter search field:')
searchTerm = input('Please enter search term:')
    
query_body = {
  "query": {
    "bool": {
      "must": {
        "match": {      
          searchField: searchTerm
        }
      }
    }
  }
}

elastic_client = Elasticsearch(hosts=["http://localhost:9200"])
result = elastic_client.search(index="books", body=query_body)
for entry in result['hits']['hits']:    
    print(entry['_source'])
    print()