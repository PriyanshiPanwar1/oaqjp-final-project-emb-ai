"""
Emotion Detection module using Watson NLP API.
"""

import json
import requests


def emotion_detector(text_to_analyse):
    """
    Analyze emotion from input text using Watson NLP service.
    """

    if text_to_analyse is None or text_to_analyse.strip() == "":
        return None

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(
        url,
        json=input_json,
        headers=headers,
        timeout=10
    )

    if response.status_code != 200:
        return None

    formatted_response = json.loads(response.text)

    emotions = formatted_response[
        "emotionPredictions"
    ][0]["emotion"]

    return emotions