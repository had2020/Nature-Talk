import openai

# Set your OpenAI API key

# Generate response from ChatGPT
response = openai.Completion.create(
    engine="text-davinci-003",  # Choose the engine (e.g., text-davinci-003)
    prompt="What is the capital of France?",
    max_tokens=50
)

# Print the generated response
print(response.choices[0].text.strip())