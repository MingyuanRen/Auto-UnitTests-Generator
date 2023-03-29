import openai

# Set up the OpenAI API client
openai.api_key = "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"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        training_file="path/to/my_dataset.jsonl",
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