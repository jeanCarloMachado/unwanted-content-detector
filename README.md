# unwanted_content_detector

A library to detect undesired, unbranded, or harmful content

## Usage

In python:


```sh
pip install unwanted-content-detector
```

Minimal

```py
from unwanted_content_detector import Detector
detector = Detector(models=['hatefult_content_generic_distil_bert_finetuned'])
if detector.is_unwanted('content generated by llm'):
    print("Wont continue")
```

With a dataframe
```py

spark_df.with_column('is_rejected', lambda row: detector.is_unwanted)
```

In the terminal

```sh
detector_cli detector is_unwanted 'test'

[Out]
Inference result:  UNWANTED_CONTENT
True
```

## Models

| Model name            | size (mb) 
|-----------------------|-----------
| distilbert-finetuned | 3 gb

## Training 

Fine tunning

```py
from unwanted_content_detector import Detector
model = Detector({'data_source': df}).train()
```


```
./cli.py train
```


## Target Architecture / Features 

- multiple Swappable models
- multiple evaluation datasets
- possibility of configuring a custom personal dataset to fine tune
- Single performance evaluation criteria

## Use cases it could be applied to

- detecting the generation of harmful content from LLMs
- preventing harmful prompts to be injected into LLMs
- using it as a validator of content being generated according to the brand guidelines


## Liability

This tool aims to help you to detect harmful content but it is not meant to be used as the final decision maker alone. 
