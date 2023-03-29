import openai
import os

# Set up the OpenAI API client
api_key = os.environ["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"]
openai.api_key = api_key

def generate_text(prompt, model="text-davinci-002", max_tokens=100):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7,
    )

    generated_text = response.choices[0].text.strip()
    return generated_text

def main():
    while True:
        prompt = input("Enter a prompt: ")
        if prompt.lower() == "exit":
            break

        generated_text = generate_text(prompt)
        print(f"Generated text: {generated_text}\n")
        generated_text = generate_text(prompt)
        print(f"Generated text: {generated_text}\n")

if __name__ == "__main__":
    main()
