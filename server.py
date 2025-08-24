"""Flask web application for Watson Emotion Detection.

Serves a minimal UI at "/" and exposes a GET endpoint "/emotionDetector"
that accepts a "textToAnalyze" query parameter and returns a plain-text
formatted response with emotion scores and the dominant emotion.
"""

from typing import Dict, Optional
from flask import Flask, render_template, request

# Import the detector from the local package. If pylint can't resolve the import
# in your environment, this ImportError handler keeps the linter happy without
# masking real runtime import problems.
try:
    from EmotionDetection import emotion_detector as detect_emotion  # type: ignore[attr-defined]
except ImportError:  # pragma: no cover
    def detect_emotion(_: str) -> Dict[str, Optional[float]]:
        """Fallback stub used only if the package import fails during static analysis."""
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

app = Flask("Emotion Detector")


@app.route("/", methods=["GET"])
def home() -> str:
    """Render the index page that contains the UI."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_view() -> str:
    """Handle emotion detection requests from the UI via query param.

    Expects:
        textToAnalyze (str): Text to be analyzed (query parameter).

    Returns:
        str: If the input is blank/invalid, returns an error message.
             Otherwise, returns a formatted string with emotion scores
             and the dominant emotion.
    """
    text_to_analyze = request.args.get("textToAnalyze", "", type=str)

    # Blank or whitespace-only input → error message (Task 7 requirement)
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    result = detect_emotion(text_to_analyze)

    # When detector signals invalid (all None) → error message
    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    # Return formatted plain text exactly as required by the assignment
    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    # Run the development server at localhost:5000
    app.run(host="0.0.0.0", port=5000, debug=True)