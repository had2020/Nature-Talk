import requests

# Define your API key
api_key = "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"

# Define the endpoint URL
endpoint = "https://api.openai.com/v1/engines/text-davinci-003/completions"

# Define the prompt
prompt = "Q: What is the meaning of life?\nA: The meaning of life is"

# Define the data payload
data = {
    "prompt": prompt,
    "max_tokens": 50,  # Maximum number of tokens in the response
    "temperature": 0.7,  # Controls the randomness of the response
    "api_key": api_key
}

# Send the request to the API
response = requests.post(endpoint, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Print the completion
    print(response.json()["choices"][0]["text"])
else:
    # Print the error message
    print("Error:", response.text)