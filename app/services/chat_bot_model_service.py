import os

import google.generativeai as genai
from google.generativeai import ChatSession
from ..services.nlp_service_lemmatization import NLPServiceLemmatization
from ..services.vector_db_service import query

genai.configure(api_key="AIzaSyBY_1om9oW2vJubvmLcn4gyV2Uk0auUUro")

generation_config = {
    "temperature": 0.1,
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


def iterate_success_case(context_info: dict):
    message = ""
    for idx, info in enumerate(context_info["documents"]):
        title = context_info["metadatas"][idx]["title"]
        message += f"Caso de exito {idx + 1}: {title} - {info}  \n"
    return message


def message_with_context(user_message: str, context: dict):
    return f"El mensaje de usuario es el siguiente después de este símbolo ‘:’ {user_message}" \
           "Estos son los casos de éxitos más relacionados al mensaje del usuario enumerados y puestos en el formato ‘nombre’ - ‘contenido’:" \
           f"{iterate_success_case(context)}"


def message_without_context(user_message: str):
    return f"El mensaje de usuario es el siguiente después de este símbolo ‘:’ {user_message}"


def generate_model_message(user_message: str, context: dict, is_search):
    if is_search:
        return message_with_context(user_message, context)
    else:
        return message_without_context(user_message)


def chat_model(chat_data: dict):
    user_message = chat_data["text"]
    history = chat_data["history"]
    is_search = chat_data['is_search']
    documents_context = chat_data["search_context"] if is_search else None


    chat_session = generate_chat_history(history)
    model_message = generate_model_message(user_message, documents_context, is_search)
    print(model_message)
    response = chat_session.send_message(model_message)
    return response.text


def get_success_case_list(relational_success_case_info: dict) -> list:
    relational_info = []
    for idx, metadata in enumerate(relational_success_case_info["metadatas"]):
        info = {
            "link": f"https://docs.google.com/presentation/d/{relational_success_case_info['ids'][idx]}",
            "title": metadata["title"]
        }
        relational_info.append(info)
    return relational_info


def generate_chat(request: dict):
    try:
        is_search = NLPServiceLemmatization().is_search(request['text'])
        request['is_search'] = is_search
        if is_search:
            request['search_context'] = query(request)
        model_response = chat_model(request)

        return {
            "model_response": model_response,
            "is_search": is_search,
            "relational_success_cases": get_success_case_list(request['search_context']) if is_search else None
        }
    except Exception as e:
        print(e)
        return None
