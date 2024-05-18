from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
   return render_template('chat.html')

@app.route('/mission')
def chat():
   return render_template('mission.html')

@app.route('/qna')
def chat():
   return render_template('qna.html')

@app.route('/about')
def chat():
   return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)