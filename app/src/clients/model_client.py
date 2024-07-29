from flask import current_app
import google.generativeai as genai
import logging

logger = logging.getLogger(__name__)


class ModelClient:
    model = None
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ModelClient, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            try:
                genai.configure(api_key=current_app.config['GENIE_API_KEY'])
                generation_config = {
                    "temperature": 0.1,
                    "top_p": 0.95,
                    "top_k": 64,
                    "max_output_tokens": 500,
                    "response_mime_type": "text/plain",
                }

                self.model = genai.GenerativeModel(
                    model_name="gemini-1.5-flash",
                    generation_config=generation_config,
                    system_instruction="Eres un asistente de busqueda de casos de éxito de una empresa de software."
                                       " Si no te piden describir un caso de éxito, respondes al mensaje y al final "
                                       "te ofreces para realizar una búsqueda. Si te piden describir un caso de éxito, "
                                       "lo describes brevemente mencionando que ese caso de éxito es la mejor"
                                       " coincidencia con su búsqueda."
                )
                logger.info("Initialized model client")
            except Exception as e:
                logger.error(f"Error initializing model client. Error: {e}")

    def get_model(self):
        return self.model
