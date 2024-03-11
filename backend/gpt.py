def extract_features(client, user_input):
# Call the OpenAI API to generate completions
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt="List the features in a comma-separated format the tenant looks for in a house, separating each " +
            "feature with a comma. Make the features as simple as possible. " 
            + "This is what the tenant says: " + user_input,
    )
    generated_text = response.choices[0].text.strip()
    return generated_text

def topic(client, input):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt="Is the user talking about housing preference or lease tutorials? If housing preference, return 0. Otherwise, return 1. This is user input: " + input,
    )
    generated_text = response.choices[0].text.strip()
    print(generated_text)
    return generated_text


def gpt_tutorial(client, message):
    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "I am talking about lease in Canada." + message + "Also, give me the https to read more and understand better your response."}
            ]
    )
    generated_text = response.choices[0].message.content.strip()
    return generated_text