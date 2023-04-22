import pandas as pd

def test_dataframe():
    from unwanted_content_detector import Detector
    detector = Detector()
    df = pd.DataFrame({"text": [
        "this is hate speech",
        "We should all do our part to protect the environment.",
        'Everyone has the right to love who they want.'
    ]})

    df['is_unwanted'] = df['text'].apply(lambda x: detector.is_unwanted(x))

    print(df)