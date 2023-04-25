from pydantic import BaseModel, HttpUrl

class ResponseModel(BaseModel):
    question: str
    context_url: HttpUrl