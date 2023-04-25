import os

class Config:
    # autocomplete url
    wiki_autocomplete_url = "https://en.wikipedia.org/w/rest.php/v1/search/title"

    # log level
    log_level = int(os.getenv("LOG_LEVEL", "40"))