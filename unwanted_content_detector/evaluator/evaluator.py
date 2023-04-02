import random

from data.loader import load_data
from unwanted_content_detector.entities import Label


def random_guess():
    return random.choice([Label.UNWANTED_CONTENT.value, Label.SAFE_CONTENT.value])


class Evaluator:

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



