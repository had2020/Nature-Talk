from flask import Flask, render_template, request

app = Flask(__name__)

# rendering page templates
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
   return render_template('chat.html')

@app.route('/mission')
def mission():
   return render_template('mission.html')

@app.route('/qna')
def qna():
   return render_template('qna.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/accounts')
def accounts():
   return render_template('account.html')

@app.route('/signed_in')
def signed_in():
   return render_template('signed_in.html')

# chat page methods
@app.route('/logined')
def logined():
   return render_template('signed_in.html')

if __name__ == '__main__':
  app.run(debug=True)