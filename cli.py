#!/usr/bin/env python3

class UnwantedContentDetectorCLI:
    def __init__(self):
        from unwanted_content_detector.evaluator.evaluator import Evaluator
        self.evaluator = Evaluator
        from unwanted_content_detector.models.distilbert_finetuned.train import train
        self.train = train

        from unwanted_content_detector.detector import Detector
        self.detector = Detector

        from unwanted_content_detector.models.upload import upload_model, download_model
        self.upload_model = upload_model

        self.download_model = download_model

def main():
    import fire
    fire.Fire(UnwantedContentDetectorCLI)

if __name__ == "__main__":
    main()
