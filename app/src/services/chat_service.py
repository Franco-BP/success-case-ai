from ..services.nlp_service import is_search
from ..services.vector_db_service import query
from ..clients.model_client import ModelClient


def generate_chat_history(history_chat: list):
    model = ModelClient().get_model()
    return model.start_chat(
        history=history_chat
    )


def iterate_success_case(context_info: dict):
    message = ""
    for idx, info in enumerate(context_info.get("documents", [])):
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
    history = chat_data.get("history", [])
    search = chat_data['is_search']
    documents_context = chat_data.get("search_context", {})

    chat_session = generate_chat_history(history)
    model_message = generate_model_message(user_message, documents_context, search)
    response = chat_session.send_message(model_message)
    return response.text


def get_success_case_list(relational_success_case_info: dict) -> list:
    relational_info = []
    for idx, metadata in enumerate(relational_success_case_info["metadatas"]):
        info = {
            "link": f"https://docs.google.com/presentation/d/{relational_success_case_info['ids'][idx]}",
            "title": metadata["title"],
            "distance": relational_success_case_info["distances"][idx]
        }
        relational_info.append(info)
    return relational_info


def generate_chat(request: dict):
    try:
        search = is_search(request['text'])
        request['is_search'] = search
        if search:
            request['search_context'] = query(request)
        model_response = chat_model(request)

        return {
            "model_response": model_response,
            "is_search": search,
            "relational_success_cases": get_success_case_list(request['search_context']) if search else None
        }
    except Exception as e:
        print(e)
        return None
