from flask import Flask, jsonify, request, abort
import requests
from flask_cors import CORS
from utils.logger import log
from utils.exceptions import ValidationError
from config import Config
from models.response_model import ResponseModel
from bs4 import BeautifulSoup
from qa_model.tinyroberta import QAModel

app = Flask(__name__)
CORS(app)


def get_context(context_url):
    page = requests.get(context_url)
    txt = page.text
    soup = BeautifulSoup(txt, "lxml")
    for item in soup.find_all(class_="reflist"):
        item.extract()
    for item in soup.select("script"):
        item.extract()
    for item in soup.select("Further_reading"):
        item.extract()
    for item in soup.select("See_also"):
        item.extract()
    body = soup.find(id="mw-content-text")
    if body:
        return body.get_text(" ", strip=True)


@app.get("/")
def healthcheck():
    log.debug("Hit healthcheck endpoint")
    return {"version": "1.0.0"}


@app.get("/topics")
def get_topics():
    try:
        url = Config.wiki_autocomplete_url
        find = request.args.get("q", default="", type=str)
        limit = request.args.get("limit", default=10, type=int)
        params = {"q": find, "limit": limit}
        res = requests.get(url, params=params)
        data = res.json()
        pages = data["pages"]
        topics = []
        for item in pages:
            name = item["title"]
            description = item["description"]
            topic_url = f"https://en.wikipedia.org/wiki/{item['key']}"
            thumbnail = item.get("thumbnail")
            image_url = thumbnail["url"] if thumbnail else None
            topic = {
                "name": name,
                "description": description,
                "topic_url": topic_url,
                "image_url": image_url,
            }
            topics.append(topic)
        return jsonify(topics)
    except Exception as e:
        log.error(f"Error: {str(e)}")
        abort(500)


@app.post("/response")
def response():
    try:
        body = request.json or {}
        res_model = ResponseModel(**body)
        context = get_context(context_url=res_model.context_url)
        qa = QAModel()
        res = qa.predict(question=res_model.question, context=context)
        response_data = {"answer": res["answer"], "score": res["score"]}
        return response_data
    except ValueError as e:
        log.error(f"Error: {str(e)}")
        abort(400)
    except ValidationError as e:
        log.error(f"Error: {str(e)}")
        abort(400)
    except Exception as e:
        log.error(f"Error: {str(e)}")
        abort(500)


if __name__ == "__main__":
    # This server is only for local/debug
    app.run(port=8080, debug=True)
