import spacy
from unidecode import unidecode
from ..utils.nlp_util import NLPUtil

def is_search(text):
    """
    Determines whether the user intents to search success cases using lemmatization.

    Args:
        text: The user's text.

    Returns:
        bool: True if the intention is to search, False if it's not.
    """

    # Preprocessing of the text
    text = unidecode(text)
    doc = NLPUtil()._nlp(text)
    #filtered_tokens = [token for token in doc if token.text.lower() not in NLPUtil()._stop_words]

    # Lemmatization
    tokens_lemmatized = [token.lemma_.lower() for token in doc]

    # Verify if there is any key words
    for token in tokens_lemmatized:
        if token in NLPUtil()._key_words or any(word == token for word in NLPUtil()._key_words):
            print(True)
            return True
    print(False)
    return False
