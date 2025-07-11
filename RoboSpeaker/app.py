from flask import Flask, request, render_template
import pyttsx3
import threading

app = Flask(__name__)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        threading.Thread(target=speak, args=(text,)).start()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
