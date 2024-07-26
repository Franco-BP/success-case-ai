import os

import google.generativeai as genai
from google.generativeai import ChatSession

genai.configure(api_key="AIzaSyBY_1om9oW2vJubvmLcn4gyV2Uk0auUUro")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 500,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="Eres un asistente de busqueda de casos de éxito de una empresa de software. Si no te piden describir un caso de éxito, respondes al mensaje y al final te ofreces para realizar una búsqueda. Si te piden describir un caso de éxito, lo describes brevemente mencionando que ese caso de éxito es la mejor coincidencia con su búsqueda."
)


def generate_chat_history(history_chat: list) -> ChatSession:
    return model.start_chat(
        history=history_chat if history_chat is not None else []
    )


def generate_model_message(user_message: str):
    return f"{user_message}"


def chat_model(chat_data: dict):
    user_message = chat_data["text"]
    history = chat_data["history"]

    chat_session = generate_chat_history(history)
    model_message = generate_model_message(user_message)
    response = chat_session.send_message(model_message)
    return {
        "response": response.text
    }
