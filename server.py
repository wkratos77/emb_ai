from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")
# serve the UI
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")
# endpoint the JS calls
@app.route("/emotionDetector", methods=["GET"])
def emotionDetector():
    # IMPORTANT: match the query param name used by mywebscript.js
    text_to_analyze = request.args.get("textToAnalyze", "", type=str)

    # If no query param, just show the page (lets you visit the URL directly)
    if not text_to_analyze:
        return render_template("index.html")
    # Run the model
    result = emotion_detector(text_to_analyze)
    # Return the EXACT formatted plain-text line the page expects
    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
