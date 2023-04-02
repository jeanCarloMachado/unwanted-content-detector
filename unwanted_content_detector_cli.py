

class UnwantedContentDetectorCLI:
    def __init__(self):
        from unwanted_content_detector.evaluator.evaluator import Evaluator
        self.evaluator = Evaluator
        from unwanted_content_detector.models.train import train
        self.train = train

if __name__ == "__main__":
    import fire
    fire.Fire(UnwantedContentDetectorCLI)
