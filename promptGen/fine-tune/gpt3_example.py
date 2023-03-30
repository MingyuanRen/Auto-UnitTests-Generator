import openai

# Set up the OpenAI API client
# openai.api_key = "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"
openai.api_key = input("Enter OpenAI API Key")
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

# Example usage
prompt = "Translate the following English text to French: 'what example should I do with'"
response = generate_response(prompt)
print(response)