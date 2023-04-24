from pydantic import BaseModel

class TopicModel(BaseModel):
    name: str
    description: str
    image_url: str
    topic_url: str


