from dotenv import load_dotenv
import cohere
import os
import orjson

# load .env file
load_dotenv()
api_key = os.getenv("COHERE_API_KEY")

# tokenize cohere api
co = cohere.Client(api_key)

# load user query json
with open('example_user_queries.json') as user_file:
    user_input = user_file.read()
# load tenant posting data json
with open('example_posting.json') as data_file:
    houses_input = data_file.read()

# parse json data sets
user_query = orjson.loads(user_input)
houses = orjson.loads(houses_input)

user_pref = user_query[0].get('preferences')

# extract houses description
docs = []
for house in houses:
    docs.append(house.get('description'))

results = co.rerank(query=user_pref, documents=docs, top_n=3, model='rerank-english-v2.0')

for idx, r in enumerate(results):
    print(f"Document Rank: {idx + 1}, Document Index: {r.index}")
    print(f"Document: {r.document['text']}")
    print(f"Relevance Score: {r.relevance_score:.2f}")
    print("\n")
