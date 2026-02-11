from flask import Flask, jsonify, request
from flasgger import Swagger
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)
swagger = Swagger(app)
@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    text = request.get_json()["text"]
    return emotion_detector(text)


# curl -X POST http://127.0.0.1:5000/emotionDetector \
#   -H "Content-Type: application/json" \
#   -d '{"text": "I love my life"}'

if __name__ == '__main__':
   app.run(debug=True)