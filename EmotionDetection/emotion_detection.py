import requests  # Import the requests library to handle HTTP requests
import json
def emotion_detector(text_to_analyse): 
     """Call Watson NLP EmotionPredict API on input text.

    Args:
        text_to_analyse (str): The input text to analyze.

    Returns:
        dict: Dictionary with emotion scores (anger, disgust, fear, joy, sadness)
              and the dominant_emotion. Returns None values if input is invalid.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the Watson EmotionPredict service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    EMPTY = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }
    # Short-circuit obvious blanks (spaces, empty, None)
    if not text_to_analyse or not str(text_to_analyse).strip():
        return EMPTY
    try:
        resp = requests.post(url, json=myobj, headers=header)  # Send a POST request to the API with the text and headers
        if resp.status_code == 400:
            return EMPTY
        resp.raise_for_status()  # raise for other HTTP errors
        data = json.loads(resp.text)
        emotions = data['emotionPredictions'][0]['emotion']
        dominant = max(emotions, key=emotions.get) if emotions else None
        return {
            'anger': emotions.get('anger'),
            'disgust': emotions.get('disgust'),
            'fear': emotions.get('fear'),
            'joy': emotions.get('joy'),
            'sadness': emotions.get('sadness'),
            'dominant_emotion': dominant
        }
    except Exception:
        # Any networking/parse error → safe fallback required by spec
        return EMPTY