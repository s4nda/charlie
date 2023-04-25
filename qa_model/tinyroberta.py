from transformers import pipeline


class QAModel:
    model_name = "deepset/tinyroberta-squad2"

    def __init__(self):
        self.nlp = pipeline(
            "question-answering", model=self.model_name, tokenizer=self.model_name
        )

    def predict(self, question, context):
        res = self.nlp({"question": question, "context": context})
        return dict(res)  # type:ignore
