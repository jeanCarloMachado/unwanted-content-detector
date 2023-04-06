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
- Single performance evaluation criteria



## Liability

This tool aims to help you to detect harmful content but it is not meant to be used as the final decision maker alone. 
