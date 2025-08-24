# Emotion Detection Web Application

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![Watson NLP](https://img.shields.io/badge/Watson%20NLP-EmD-red)
[![Pylint](https://img.shields.io/badge/pylint-10%2F10-brightgreen)]()
[![Tests](https://img.shields.io/badge/tests-passing-success)]()

Final Project for **AI-Based Web Application Development and Deployment** (Embeddable Watson AI).
This app integrates the **Watson NLP EmotionPredict API** to analyze text and return five emotions
(**anger, disgust, fear, joy, sadness**) plus the **dominant emotion**. Built with **Flask**.

---

## ✨ Features
- Watson NLP **EmotionPredict** integration (no local model required)
- Clean API wrapper with **error handling** (blank input → friendly message)
- **Flask** web UI (GET endpoint compatible with provided `index.html` + `mywebscript.js`)
- **Unit tests** for core behavior
- Passes **Pylint** static analysis (10/10 with docstrings)

---

## 📦 Project Structure
emd-ai/
├─ EmotionDetection/   
│ └─ emotion_detection.py # Core Watson API integration + error handling     
│ └─ __init__.py # Core Watson API integration + error handling    
├─ templates/     
│ └─ index.html # Provided UI (no edits required)      
├─ static/     
│ └─ mywebscript.js # Provided JS (no edits required)     
├─ server.py # Flask app (routes: / and /emotionDetector)    
├─ test/    
│ └─ test_emotion_detection.py # Unit tests   
└─ README.md    

---

## 🚀 Run

```bash```
python3 server.py


App runs on http://127.0.0.1:5000 (lab preview may proxy this).

UI: open / to load index.html.

Response format (example):

For the given statement, the system response is 'anger': 0.006, 'disgust': 0.003,
'fear': 0.009, 'joy': 0.968 and 'sadness': 0.049. The dominant emotion is joy.

---

## 🧪 Tests

```bash```
python3 -m unittest test_emotion_detection.py

Expected: all tests pass for dominant emotions:

- glad → joy

- mad → anger

- disgusted → disgust

- sad → sadness

- afraid → fear

---

## 🛡️ Error Handling

Blank or whitespace-only input → backend returns all None from the detector and the server responds with:

```Invalid text! Please try again!```


If the Watson endpoint returns 400, detector returns the same all-None structure by design.

---

## 🧹 Static Code Analysis (Pylint)

```bash```
pylint server.py


Tips to get 10/10:

- Add module and function docstrings (already included)

- Use snake_case function names

- Avoid unused imports / long lines

---

## 🔧 Implementation Notes

Detector endpoint & headers

- URL: https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict

- Header: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

- Payload: {"raw_document": {"text": "<TEXT>"}}

Server routes

- GET / → renders index.html

- GET /emotionDetector?textToAnalyze=<TEXT> → returns formatted plain text
