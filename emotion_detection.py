import requests
import json

def emotion_detector(text_to_analyze):
    # The URL for the Watson Emotion Predict service 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # The required headers for the NlpService 
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # The input json format using the variable text_to_analyze 
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Sending the POST request to the Watson NLP service
    response = requests.post(url, json=input_json, headers=headers)
    
    # Returning the text attribute of the response object as required
    return response.text
