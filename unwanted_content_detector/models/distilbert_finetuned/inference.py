# inspiration documentation https://huggingface.co/docs/transformers/tasks/sequence_classification
import torch

from transformers import AutoModelForSequenceClassification, AutoTokenizer
from .train import MODEL_NAME


def infer(text):
    print(f"Loading model {MODEL_NAME}")
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_class_id = logits.argmax().item()
    return (model.config.id2label[predicted_class_id])



