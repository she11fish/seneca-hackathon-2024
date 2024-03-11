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
with open('features.json') as user_file:
    user_input = user_file.read()
# load tenant posting data json
with open('houses_data.json') as data_file:
    houses_data = data_file.read()

# parse json to python dictionaries
user_query = orjson.loads(user_input)
houses = orjson.loads(houses_data)

# remove images field from the data input
house_queries = []
for query in houses:
    new_query = {}
    for key in query.keys():
        if key in user_query.keys() or key == 'description':
            new_query.update({key: query.get(key)})
    house_queries.append(new_query)

# convert rental listing data to one string
docs = []
for query in house_queries:
    docs.append(str(query))

# convert user input to one string
user_input = str(user_query)

result = co.rerank(query=user_input, documents=docs, top_n=5, model='rerank-multilingual-v2.0')

for idx, r in enumerate(result):
    print(f"Document Rank: {idx + 1}, Document Index: {r.index}")
    print(f"Document: {r.document['text']}")
    print(f"Relevance Score: {r.relevance_score:.2f}")
    print("\n")
