import requests
import json


rec_data = {
    "article_id": "0"
} 

search_data = {
    "keyword": "hello"
}

viewRecent_data = {
    "date": "2023-02-22"
}

Recommendations = requests.post('http://localhost:5000/Recommendations', data= rec_data)
Recommendationsjson = json.loads(Recommendations.text)
print(Recommendationsjson)

searched_req = requests.post('http://localhost:5000/Search', data= search_data)
searchedJson = json.loads(searched_req.text)
print(searchedJson)

viewRecent_req = requests.post('http://localhost:5000/Recent', data= viewRecent_data)
viewRecentJson = json.loads(viewRecent_req.text)
print(viewRecentJson)
