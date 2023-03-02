import pandas as pd
import joblib
import numpy as np
# import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# VARIABLES
global org_data
global similarity
org_data = pd.read_csv("data/processed_data.csv")
org_data["id"] = org_data["id"].apply(lambda x: str(x))
train_data = pd.read_csv('data/Training.csv')
# similarity = joblib.load('model/newsapi_articles_cosinesimilarity.pkl')

# TFIDF Search
vectorizer = TfidfVectorizer()
data_vector = vectorizer.fit_transform(org_data["author"]+ org_data["title"]+ org_data["publishedAt"])

# TFIDF Recommendations
rec_vector = TfidfVectorizer(stop_words='english')
tfidf_matrix = rec_vector.fit_transform(train_data['tags'])

# calculating similarity
similarity = cosine_similarity(tfidf_matrix)

# for loading recommendations
def load_recommendations(id):

    # getting inferencing
    scores = similarity[int(id)]
    # print(scores)
    #  Find the top 3 most similar documents
    top_indices = np.argsort(scores)[::-1][1:21]

    # extracting data of recommended documents
    heads = []
    for i in top_indices:
        dictionary = {
            "id": str(i), 
            "title": org_data['title'].iloc[i],
            "author": org_data['author'].iloc[i],
            "headline": org_data['description'].iloc[i],
            "publishedAt": org_data['publishedAt'].iloc[i],
            "content": org_data['content'].iloc[i],
            "url": org_data['url'].iloc[i]
        }
        heads.append(dictionary)
    return heads

# if the request is to get articles of recently posted.
def load_searched(keyword):
    # getting similarity
    string_vector = vectorizer.transform([str(keyword)])
    cosine_similarities = (cosine_similarity(data_vector, string_vector)).flatten()
    
    #  Find the top 3 most similar documents
    top_indices = np.argsort(cosine_similarities)[::-1][:10]

    # with open("top.json", 'w') as xtext:
    #     json.dump(top_indices.tolist(), xtext)

    # print(cosine_similarities.tolist())
    heads = []
    for i in top_indices:
        dictionary = {
            "id": str(i), #.values[0], 
            "title": org_data['title'].iloc[i], #.values[0],
            "author": org_data['author'].iloc[i],
            "headline": org_data['description'].iloc[i], #.values[0],
            "publishedAt": org_data['publishedAt'].iloc[i], #.values[0],
            "content": org_data['content'].iloc[i], #.values[0],
            "url": org_data['url'].iloc[i] #.values[0]
        }
        heads.append(dictionary)
    return heads

# view recent dataed articles
def load_recent(date= "2023-02-17"):
    new = org_data[org_data["publishedAt"] >= date].tail(20)
    heads = []
    for i in range(len(new)):
        dictionary = {
            "id": str(org_data[org_data['id']==new['id'].iloc[i]].head(1).index[0]), 
            "title": new['title'].iloc[i],
            "author": new['author'].iloc[i],
            "headline": new['description'].iloc[i],
            "publishedAt": new['publishedAt'].iloc[i],
            "content": new['content'].iloc[i],
            "url": new['url'].iloc[i]
        }
        heads.append(dictionary)
    return heads