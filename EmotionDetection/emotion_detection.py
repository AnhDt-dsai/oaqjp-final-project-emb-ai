import requests
import json

def parse_output(output):
    output = json.loads(output)
    return output["emotionPredictions"][0]["emotion"]

def emotion_detector(text_to_analyze):
    response = requests.post(url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
                            headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
                            json = { "raw_document": { "text": text_to_analyze } })
    return parse_output(response.text)

if __name__ == "__main__":  
    print(emotion_detector("I love this new technology"))