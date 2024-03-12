from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import json

# Sample data
def recommend(dct):
    with open('rentsData/data.json', 'r') as file:
        data = json.load(file)
    
    raw_data = pd.DataFrame(data)
    cleaned_data = [{k: v for k, v in d.items() if k not in ['images', 'landlord_name']} for d in data]
    df = pd.DataFrame(cleaned_data)
    print(df.head())
        
    # data = {
    #     'price': [100000, 200000, 150000, 120000, 180000],
    #     'preferences': ['gym, pool', 'pool, park', 'park', 'gym', 'pool'],
    #     'furnished': [1, 0, 1, 0, 1],
    #     'location': ['city', 'suburb', 'city', 'suburb', 'city'],
    #     'rooms_available': [2, 3, 1, 2, 1],
    #     'building_type': ['apartment', 'house', 'apartment', 'house', 'apartment'],
    #     'label': [0, 1, 2, 3, 4]  # Target labels for each data point
    # }

    # df = pd.DataFrame(data)
    text_preprocessor = Pipeline([
        ('vect', CountVectorizer(tokenizer=lambda x: x.split(','))),
        ('tfidf', StandardScaler(with_mean=False))  # Sparse matrix with_mean=False for compatibility
    ])
    
    # Preprocessing pipeline
    preprocessor = ColumnTransformer(transformers=[
        ('preferences', CountVectorizer(tokenizer=lambda x: x.split(',')), 'description'),
        # ('location', CountVectorizer(tokenizer=lambda x: x.split(',')), ['location']),
        ('location', CountVectorizer(tokenizer=lambda x: x.split(',')), 'location'),  # Apply CountVectorizer to 'location'
        ('house_type', OneHotEncoder(), ['house_type']),
        # ('description', text_preprocessor, ['location', 'description']),
        ('furnished', OneHotEncoder(drop='if_binary'), ['furnished']),  # Handle furnished feature
        ('numeric', StandardScaler(), ['price', 'num_of_room_availables'])
    ])

    # KNN model
    knn = KNeighborsClassifier(n_neighbors=3)

    # Full pipeline
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('knn', knn)
    ])

    # Training
    X = df.drop(columns=['label'])  # Remove the target column
    y = df['label']
    print(X)
    print(y)
    pipeline.fit(X, y)

    # Example prediction
    # new_data = {
    #     'price': [180000],
    #     'preferences': ['gym'],
    #     'location': ['suburb'],
    #     'rooms_available': [2],
    #     'building_type': ['house']
    # }
    # new_df = pd.DataFrame(new_data)
    new_df = pd.DataFrame(dct)
    print(new_df)
    # Find the indices and distances of the 3 nearest neighbors
    distances, indices = pipeline.named_steps['knn'].kneighbors(pipeline.named_steps['preprocessor'].transform(new_df))

    # Get the labels of the 3 nearest neighbors
    nearest_neighbors_labels = y.iloc[indices[0]]
    print("Labels of the 3 nearest neighbors:", nearest_neighbors_labels.tolist())
    top_data_list = []
    for index in indices[0]:
        top_data_list.append(raw_data.iloc[index].to_dict())
    # top_data = raw_data[raw_data['label'].isin(nearest_neighbors_labels)]
    # print(top_data)
    return top_data_list


# dct = {
#     'price': [180000],
#     'description': ['gym'],
#     'location': ['suburb'],
#     'num_of_room_availables': [2],
#     'house_type': ['Condo'],
#     'furnished': [1]
# }

# recommended_data = recommend(dct)
# print(recommended_data)