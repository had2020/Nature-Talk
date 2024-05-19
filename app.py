from flask import Flask, render_template, request
from models import login_func, save_message # imports fuction from models.py

# variables
username = ""
password = ""

has_logined = False

app = Flask(__name__)

# rendering page templates
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/chat')
def chat():
   if has_logined == False:
      return render_template('login_waring.html')
   if has_logined == True:
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
   if has_logined == True:
      return render_template('account.html')
   else:
      return render_template('login_waring.html')

@app.route('/signed_in')
def signed_in():
   return render_template('signed_in.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/test_vid')
def test_vid():
   return render_template('test_vid.html')

@app.route('/sus_music')
def sus_music():
   return render_template('sus_music.html')

# chat and account page methods
@app.route('/send_message', methods=['POST'])
def send_message():
    # Access the submitted message from the request form
    message = request.form['message']
    save_message(username, message)

    add_history()

    return render_template('chat.html', message_sent=True)  # Pass data to template

@app.route('/logined', methods=['POST'])
def logined():
   username = request.form['username']
   password = request.form['password']
   print(username, password)

   login_func(username, password)

   global has_logined
   has_logined = True

   return render_template('signed_in.html')

# Append the message to the chat history
def add_history():
   print("add history function ran")
   text = "Hello, World!"
   html = render_template('chat.html')
   new_html = html.replace("Old text", text)
   return new_html

if __name__ == '__main__':
  app.run(debug=True)