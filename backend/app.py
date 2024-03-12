from flask import Flask, request
import os
# from leaseExtraction.leaseExtraction import extract
from dotenv import load_dotenv
import os
from openai import OpenAI
from tutorial.resources import *
from gpt import *
from ner import *
from recommend_from_scratch import *
app = Flask(__name__)


load_dotenv()

count=0
current_topic=None
preferences={}
needed_info = None

client = OpenAI(api_key=os.getenv("GPT_API_KEY"))
extraction = ""
@app.route('/upload', methods=['POST'])
def upload_file():
    global extraction
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        filename = file.filename
        path = os.path.join("./userFile/", filename)
        file.save(path)
        extraction = extract(path)
        return 'File uploaded successfully'

@app.route('/extract', methods=['GET'])
def get_least_extraction():
    global extraction
    return extraction

@app.route('/get_response', methods=['GET'])
def get_response():
    global preferences
    global current_topic
    user_input = request.form["chat"]
    global count
    print(count)
    global needed_info
    message = ""
    topic_response = topic(client, user_input)
    print(current_topic, topic_response)
    if count == 0:
        message = "Welcome to Lease! Are you interested in discussing housing preferences or learning about lease tutorials?"
    elif count == 1 or (current_topic=="tutorial" and topic_response == "0"):
        if topic_response == "0":
            message = "Okay, what's your housing preference (Change this prompt later)."
            current_topic = "recommend"
        elif topic_response == "1":
            message = ("Here are some resources and links that can help you with lease rights education: "
                    + "\n" + r1 + "\n" + r1d + "\n" + r1u + "\n"+"\n" + 
                    r2 + "\n" + r2d + "\n" + r2u + "\n"+"\n" +
                    r3 + "\n" + r3d + "\n" + r3u + "\n"+"\n" +
                    r4 + "\n" + r4d + "\n" + r4u + "\n" + "\n" +
                    "Let me know if you have any question.") 
            current_topic="tutorial"
        else:
            message = ("Sorry, I didn't understand. Could you please repeat?")
    elif current_topic == "recommend":
        if needed_info is None:
            preferences = named_entity_extraction(user_input)
            preferences["description"] = [extract_features(client, user_input)]
            if "house_type" not in preferences:
                message = "What type of house do you prefer"
                needed_info = "house_type"
            elif "furnished" not in preferences:
                message = "Do you prefer furnished or non-furnished?"
                needed_info = "house_type"   # TODO Add more checks
        elif needed_info == "house_type":
            preferences["house_type"] = [user_input]
            if "furnished" not in preferences:
                message = "Do you prefer furnished or non-furnished?"
                needed_info = "furnished"   # TODO Add more checks
        elif needed_info == "furnished":
            preferences["furnished"] = [False] if "non" in user_input.lower().strip() else [True]

        if len(preferences) == 6:
            recommended_listings = recommend(preferences) # TODO Integrate this with hwey's function
            return {"message":"Great! let me find the perfect listing for you", "recommend":True, "recommendations":recommended_listings}
    else:
        message = gpt_tutorial(client, user_input)
    count+=1
    return {"message":message, "recommend":False}

        
if __name__ == '__main__':
    app.run(host='192.168.2.45', debug=True)