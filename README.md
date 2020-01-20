## Requirements for ElasticSearchPython

You may download ElasticSearch from this location:

    https://www.elastic.co/downloads/elasticsearch

Start ElasticSearch:

    elasticsearch-7.5.1\bin>elasticsearch
    
Using a tool like postman or CURL create the index and an entry in the index:

POST

    http://localhost:9200/books/book

Body JSON:

    {"isbn":"978-0615488233", "title":"Arash the Archer", "author":"Shahriar Bourbour", "releaseDate":"2011-06-11"}
    {"isbn":"978-1986486996", "title":"Arash: Movie Script", "author":"Shahriar Bourbour", "releaseDate":"2018-05-23"}
    

Using curl to insert:

    curl -X POST localhost:9200/books/book {"isbn":"978-0615488233", "title":"Arash the Archer", "author":"Shahriar Bourbour", "releaseDate":"2011-06-11"}
    
Using curl to query (must is like AND):    
    
    curl -X GET "localhost:9200/_search?pretty" -H 'Content-Type: application/json' -d'{"query": {"bool": {"must": [{"match": {"title":"arash"}}]}}}'
    
(should is like OR):
    
    curl -X GET "localhost:9200/_search?pretty" -H 'Content-Type: application/json' -d'{"query": {"bool": {"should": [{"match": {"title":"arash"}}, {"match": {"author":"anahita"}}]}}}'

You can then run queries in your browser or Postman this way:

    http://localhost:9200/books/_search?q=Arash

To make REST calls from Python you need the requests module. You can use the pip command or easy_install (Python 3.8 on Windows) for ex:

    cd c:\Users\shahriar\Python38\Scripts
    easy_install requests
    
Or

    pip install requests
    
## More info:

    https://towardsdatascience.com/getting-started-with-elasticsearch-in-python-c3598e718380

    
