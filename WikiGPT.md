# WikiGPT Question answering bot

## Stack

- Flask or OpenAPI
- Pydantic
- BeautifulSoup

## Endpoints

- `GET /topics?search=atlanta` to return topics from wikipedia, returns a list of dicts
- `POST /response` {"question": str, "context_url": str} to return the answer to the question

# Todo list (ordered)

- Create FastAPI or Flask API with two endpoints described above that return empty dict
- Start implementing /topics endpoint by inspecting wikipedia page
- Format /topics endpoint response to include `contextUrl`, `image` and `name`
  - Topics endpoint requires query param ?search=str
  - Add error handling if ?search is missing and return 400 error
- Implement POST /response endpoint that accepts dict with "contextUrl" and "questions"
  - Both contextUrl and questions are required, add error handling if some are missing, you can use Pydantic for validation, context should be a valid URL
  - use requests to fetch the wikipedia page, and extract the body text using .get_text(), to select the class use bs4.find('.some-class')
  - Instantiate the QuestionAnswering class and call qa.response(context, question) and return the output of this function
- Add CORS
- Add logs
- Add error handling

```python
class QuestionAnswering:
    def response(self, context, question) -> str:
        return 'ok'
```

# Deployment

We will deploy this project to vercel which requires python3.9. When typing annotations do not use list | str, use Union[list, str] instead.

`from typing import Union`

# TopicModel

Response for /topics endpoint:

- name
- description
- image_url (http://...)
- topic_url: https://en.wikipedia.org/wiki/{key}
- Remove topics that don't have a key

- Filter out the topic that has: "referred to by the same term" in the description
