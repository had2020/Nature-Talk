import openai

def send_ai_text(user_text):
    # Set your OpenAI API key
    openai.api_key = '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'

    # Generate response from ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the engine (e.g., text-davinci-003)
        prompt="What is the capital of France?",
        max_tokens=50
    )

    # Print the generated response
    print(response.choices[0].text.strip())