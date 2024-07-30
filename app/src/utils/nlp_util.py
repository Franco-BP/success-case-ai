import spacy

class NLPUtil:
    """Singleton class for NLP services"""

    _instance = None
    _stop_words = None
    _key_words = [
        "buscar", "buscame", "necesitar", "necesitame", "traer", "traeme", "obtener", "obtenme", "investigar",
        "investigame", "indagar", "indagame", "rastrear", "rastreame", "localizar", "localizame", "encontrar",
        "encuentrame", "hallar", "hallame", "detectar", "detectame", "descubrir", "descubrime", "identificar",
        "identificame", "adquirir", "adquirime", "alcanzar", "alcanzame", "capturar", "capturame", "atrapar",
        "atrapame", "recoger", "recogeme", "tomar", "tomame", "recibir", "recibeme", "ver", "veme",
        "conocer", "conoceme", "mejorar", "mejorame", "promedio", "solucion", "caso", "exito", "tecnologia",
        "resultado", "proyecto", "industria", "cliente", "offering", "desafio", "seguridad", "mejora", "equipo",
        "seguro", "mayor", "menor"]
    _nlp = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(NLPUtil, cls).__new__(cls)
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