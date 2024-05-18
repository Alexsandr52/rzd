import json
from thefuzz import process
import spacy
nlp = spacy.load("ru_core_news_sm")


def _detect_special_words(text_json):
    special_words = ['спасибо','пожалуйста','здравствуйте', 'здравствуй']
    def _detect(text):
        doc = nlp(text)
        for token in doc:
            if len(token)>=3:
                special_word, probability_special = process.extractOne(str(token), special_words)
                if probability_special>=85:
                    return True
        return False

    is_detect = False
    result = dict()
    for key, value in text_json.items():
        text_clear = value.replace(",", "")
        result_detect = _detect(text_clear)
        result[key] = result_detect
        if result_detect == True:
            is_detect=True

    return is_detect, result

def text_process(text_str):
    text_json = json.loads(text_str)

    #ищет слова, которые не соответствуют разговору служебному, возвращает есть ли такие слова и проверку каждлго предлодения для уазания ошибки
    is_detect, result = _detect_special_words(text_json)
    return is_detect

