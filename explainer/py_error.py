# gemini_explainer/explainer.py
import requests

def explain_error(error_message: str, api_key: str) -> str:
    prompt = f"Explica este error de forma clara y breve: '{error_message}'"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        raise RuntimeError(f"Error al consultar Gemini: {e}")