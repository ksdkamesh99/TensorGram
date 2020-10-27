from urllib.request import urlopen
from flask import Flask,request
app = Flask(__name__)

@app.route('/send')
def send():
	id=request.args.get('id')
	data=request.args.get('data')
	s=urlopen("https://api.telegram.org/bot1292653145:AAGr-ATBku9glUNytkiafQkpJli9OTL4NFM/sendMessage?chat_id="+str(id)+"&text="+data)
	if s.getcode()=200:
		return sent


if __name__ == "__main__":
    app.run(debug=False) 
