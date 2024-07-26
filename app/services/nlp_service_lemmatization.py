import spacy
from unidecode import unidecode


class NLPServiceLemmatization:
    """Singleton class for NLP services"""

    _instance = None
    _stop_words = None
    _key_words = ["buscar", "traer", "obtener", "investigar", "indagar", "rastrear", "localizar", "encontrar", "hallar",
                  "detectar", "descubrir", "identificar", "adquirir", "alcanzar", "capturar", "atrapar", "recoger",
                  "tomar", "recibir", "ver", "conocer", "mejorar", "promedio", "solucion", "caso", "exito",
                  "tecnologia", "resultado",
                  "proyecto", "industria", "cliente", "offering", "desafio", "seguridad", "mejora", "equipo", "seguro",
                  "mayor", "menor"]
    _nlp = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(NLPServiceLemmatization, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Ensure initialization only occurs once
        if not hasattr(self, '_initialized'):
            try:
                # Load Spanish model from SpaCy
                self._nlp = spacy.load('es_core_news_sm')
                self._stop_words = self._nlp.Defaults.stop_words
                print(f"Initialized instance.")
            except Exception as e:
                print(f"Error downloading NLTK resources: {e}")

    def is_search(self, text):
        """
        Determines whether the user intents to search success cases using lemmatization.

        Args:
            text: The user's text.

        Returns:
            bool: True if the intention is to search, False if it's not.
        """

        # Preprocessing of the text
        text = unidecode(text)
        doc = self._nlp(text)
        filtered_tokens = [token for token in doc if token.text.lower() not in self._stop_words]

        # Lemmatization
        tokens_lemmatized = [token.lemma_.lower() for token in filtered_tokens]

        # Verify if there is any key words
        for token in tokens_lemmatized:
            if token in self._key_words or any(word == token for word in self._key_words):
                print(True)
                return True
        print(False)
        return False
