import random

from data.loader import load_data
from unwanted_content_detector.entities import Label


def random_guess():
    return random.choice([Label.UNWANTED_CONTENT.value, Label.SAFE_CONTENT.value])


class Evaluator:
    """
    Performs evaluation on the complete set
    """

    def evaluate_distilbert(self):
        from unwanted_content_detector.models.distilbert_finetuned.inference import infer
        data = load_data()

        Y = data.iloc[:, -1:]
        X = data.iloc[:, 0]

        total = len(Y)
        print(f"Total items: {total}")
        correct = 0
        for i in range(total):
            result = infer(X.iloc[i, 0])
            if result == Y.iloc[i, 0].strip():
                correct += 1

        print(f"Accuracy: {correct/total}")


    def evaluate_random(self):
        data = load_data()

        Y = data.iloc[:, -1:]
        X = data.iloc[:, 0]

        total = len(Y)
        print(f"Total items: {total}")
        correct = 0
        for i in range(total):
            guess = random_guess()
            if guess == Y.iloc[i, 0].strip():
                correct += 1

        print (f"Accuracy: {correct/total}")



