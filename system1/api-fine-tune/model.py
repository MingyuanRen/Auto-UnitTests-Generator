import openai

# Replace "your-api-key" with your actual API key
openai.api_key = "your-api-key"

# Upload datasets
with open("train.jsonl", "rb") as train_file:
    train_response = openai.Dataset.create(
        file=train_file,
        purpose="fine-tuning",
    )

with open("valid.jsonl", "rb") as valid_file:
    valid_response = openai.Dataset.create(
        file=valid_file,
        purpose="fine-tuning",
    )

# Fine-tune the model
model = "text-davinci-002"  # Replace with the GPT-4 model name if available
train_dataset_id = train_response["id"]
valid_dataset_id = valid_response["id"]

fine_tuning_config = {
  "model": model,
  "dataset": {
    "train": train_dataset_id,
    "valid": valid_dataset_id,
  },
  "n_epochs": 3,
  "batch_size": 4,
  "max_grad_norm": 1.0,
  "learning_rate": 3e-5,
  "weight_decay": 0.01,
}

fine_tuning_response = openai.FineTuning.create(**fine_tuning_config)

# Use the fine-tuned model for inference
fine_tuned_model_id = fine_tuning_response["id"]

def predict_sentiment(review):
    prompt = f"Review: {review}\nSentiment:"
    response = openai.Completion.create(
        engine=fine_tuned_model_id,
        prompt=prompt,
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"].strip()

# Example usage
review = "I really enjoyed watching this movie. The acting was superb!"
sentiment = predict_sentiment(review)
print(f"Sentiment: {sentiment}")
