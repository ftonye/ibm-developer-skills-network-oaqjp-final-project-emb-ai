from flask import Flask, render_template , request
from  EmotionDetection import emotion_detector
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')    

@app.route('/emotionDetector')
def emotionDetector():
    text = request.args.get("textToAnalyze")
    json_rep = emotion_detector(text)
    #json_rep = json.loads(rep)

    output = f"For the given statement, the system response is 'anger': {str(json_rep['anger'])},"
    output += f" 'disgust': {str(json_rep['disgust'])}, 'fear': {str(json_rep['fear'])}, "
    output += f"'joy': {str(json_rep['joy'])} and 'sadness': {str(json_rep['sadness'])}. The dominant emotion is {str(json_rep['dominant_emotion'])}. "       
 
    return output
 
     
       