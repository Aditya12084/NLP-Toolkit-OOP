import nlpcloud

# Abstract base class
class NLPService:
    def __init__(self, api_key):
        self.api_key = api_key

    def process_text(self, para):
        raise NotImplementedError("Subclasses must implement this method")


# Polymorphism Example:
class SentimentAnalysis(NLPService):
    def process_text(self, para):
        client = nlpcloud.Client("finetuned-llama-3-70b", self.api_key, gpu=True)
        response = client.sentiment(para, target="NLP Cloud")
        max_label = max(response['scored_labels'], key=lambda x: x['score'])
        print("Sentiment:", max_label['label'])


class NamedEntityRecognition(NLPService):
    def process_text(self, para, search_term):
        client = nlpcloud.Client("finetuned-llama-3-70b", self.api_key, gpu=True)
        response = client.entities(para, searched_entity=search_term)

        if response['entities']:
            print("Entities found:")
            for entity in response['entities']:
                print(entity['text'])
        else:
            print("No such entity found.")


class LanguageDetection(NLPService):
    def process_text(self, para):
        client = nlpcloud.Client("python-langdetect", self.api_key, gpu=False)
        response = client.lang_detection(para)
        print("Language:", response['language'])
