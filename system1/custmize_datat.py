from transformers import PreTrainedTokenizer
from torch.utils.data.dataset import Dataset

class CustomTextDataset(Dataset):
    def __init__(self, tokenizer: PreTrainedTokenizer, file_path: str, block_size: int, delimiter: str = "==="):
        self.tokenizer = tokenizer
        self.block_size = block_size

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        input_output_pairs = [pair.strip() for pair in text.split(delimiter)]
        self.examples = tokenizer.batch_encode_plus(input_output_pairs, max_length=block_size, pad_to_max_length=True)["input_ids"]

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, i):
        return torch.tensor(self.examples[i], dtype=torch.long)

train_dataset = CustomTextDataset(tokenizer=tokenizer, file_path=train_file, block_size=128)
val_dataset = CustomTextDataset(tokenizer=tokenizer, file_path=val_file, block_size=128)

data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False, pad_to_multiple_of=128)
