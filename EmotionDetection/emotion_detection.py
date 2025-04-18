import requests, json

def emotion_detector(text_to_analyze):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    try:
        response = requests.post(URL, json=payload, headers=headers)

        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }
        response.raise_for_status()
        emotion_scores = response.json()["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        emotion_scores["dominant_emotion"] = dominant_emotion

        return emotion_scores

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e)
        }
 
"""
test_text = "I love my Ai Journey so far!" 
result = emotion_detector(test_text)
print(result)   
"""   
     
