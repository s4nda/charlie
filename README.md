# AIQuestionAnsweringBot - Charlie 

This is an API that provides question answering functionality, using machine learning models to find the answer from a given context. The models are based on the Hugging Face transformers library, and are fine-tuned on specific tasks.

## The API has two endpoints:

1. /topics: Returns a list of topics matching a given query. The topics are obtained by querying the Wikipedia autocomplete API.

2. /response: Returns the answer to a question given a context. The context is provided by scraping the wikipedia page, and the response is generated by applying a pre-trained model fine-tuned on a specific task.

## Installation

`git clone https://github.com/s4nda/charlie`

`pip install -r requirements.txt`


## Usage

To run the script, simply run the following command in your terminal:

`python app.py`

### Tools

- Flask
- BeautifulSoup
- Pydantic