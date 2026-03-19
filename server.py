from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

# Home page route
@app.route("/")
def index():
    return render_template("index.html")

# Emotion detector API
@app.route("/emotionDetector")
def emotion_detector_route():

    text_to_analyze = request.args.get('textToAnalyze')

    # Error handling for empty input
    if not text_to_analyze:
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    # Error handling if API fails
    if response is None or "joy" not in response:
        return "Invalid text! Please try again!"

    dominant_emotion = max(response, key=response.get)

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)