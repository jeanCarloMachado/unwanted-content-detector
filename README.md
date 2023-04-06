# unwanted_content_detector

A library to detect undesired, unbranded, or harmful content

## Usage

In python:

```py
from unwanted_content_detector import Detector
Detector().is_unwanted("text to be validated")
```

In the terminal

```sh
./cli.py inference infer 'text to be validated'
```

## Training 

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
