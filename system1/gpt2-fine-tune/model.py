import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config
from transformers import TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments

# Set the model type and path
model_name = "gpt2"
model_path = "output"

# Load the pre-trained GPT-2 model and tokenizer
config = GPT2Config.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Set the training and validation file paths
train_file = "train.txt"
val_file = "val.txt"

# Create the dataset objects
train_dataset = TextDataset(tokenizer=tokenizer, file_path=train_file, block_size=128)
val_dataset = TextDataset(tokenizer=tokenizer, file_path=val_file, block_size=128)

# Set up the data collator
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Set up the training arguments
training_args = TrainingArguments(
    output_dir=model_path,
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    eval_steps=400,
    save_steps=800,
    warmup_steps=500,
    evaluation_strategy="steps",
    logging_dir="./logs",
)

# Set up the trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
)

# Train the model
trainer.train()
