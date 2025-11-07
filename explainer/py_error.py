# explainer_genai.py
import os
from google import genai

def explain_error(error_message: str, api_key: str | None = None) -> str:
    """
    Devuelve una explicación breve del error consultando Gemini-1.5-flash.
    """
    api_key = api_key or os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Falta la API key de Gemini")

    client = genai.Client(api_key=api_key)

    prompt = f"Explica este error de forma clara y breve: '{error_message}' con formato para un desarrollador en terminal sin marckDown y ve directamente al grano."

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",   # o "gemini-1.5-pro"
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        raise RuntimeError(f"Error al consultar Gemini: {e}")


# demo rápida
if __name__ == "__main__":
    print(explain_error("AttributeError: module 'collections' has no attribute 'Iterable'"))