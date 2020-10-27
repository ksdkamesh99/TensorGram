
from urllib.request import urlopen
from flask import Flask,request
import requests
app = Flask(__name__)

def deparse_data(t):
    t=t.split(' ')
    t='%20'.join(t)
    return t

@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/send')
def send():
	id=request.args.get('id')
	data=request.args.get('data')
	data=deparse_data(data)
	print(data)
	s=urlopen("https://api.telegram.org/bot1292653145:AAGr-ATBku9glUNytkiafQkpJli9OTL4NFM/sendMessage?chat_id="+str(id)+"&text="+data)
	if s.getcode()==200:
		return "sent"


@app.route('/sendphoto',methods=['POST'])
def sendphoto():
	id=request.args.get('id')
	cap=request.args.get('caption')
	files=request.files['photo']
	files={'photo':files}
	s=requests.post("https://api.telegram.org/bot1292653145:AAGr-ATBku9glUNytkiafQkpJli9OTL4NFM/sendPhoto?chat_id="+str(id)+"&caption="+cap,files=files)
	print(s)
	return "sent"




if __name__ == "__main__":
    app.run()
