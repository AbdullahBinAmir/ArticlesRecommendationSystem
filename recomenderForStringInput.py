# import inpy
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

string_list = ['abduzeedo monterra sipping on sustainable and vegan wines with stylish packaging design', 'abduzeedo blueshift collective where nft meets creativity', 'aoirostudio reviving a legend the nissan 300zx fairlady in full cgi by christer stormark and szymon kubicki', 'abduzeedo beloved food magazine bon appétit, gets a fresh rebrand ', 'aoirostudio introducing the microsoft creator hub ']
random_string = 'aoirostudio'

print(random_string)

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

string_vectors = vectorizer.fit_transform(string_list)

random_string_vector = vectorizer.transform([random_string])

cosine_similarities = cosine_similarity(random_string_vector, string_vectors)

print(cosine_similarities)

most_similar_index = np.argmax(cosine_similarities)

print(most_similar_index)

most_similar_string = string_list[most_similar_index]

print(f"The random string is: {random_string}")
print(f"The most similar string in the list is: {most_similar_string}")
