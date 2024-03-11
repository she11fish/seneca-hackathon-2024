from openai import OpenAI
from dotenv import load_dotenv
import os
# Load environment variables from .env
load_dotenv()
client = OpenAI(api_key= os.getenv("API_KEY"))
def extract_features(input):
# Call the OpenAI API to generate completions
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt= "Put it in a numbered list with minimal words. Separate the rules for tenants and for landlords. " + input,
    )
    generated_text = response.choices[0].text.strip()
    return generated_text