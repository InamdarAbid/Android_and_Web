from flask import Flask, request, jsonify,render_template
import os
from firebase import firebase
import pyrebase
import base64
import webbrowser
import urllib
import requests 
app = Flask(__name__)


APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 

@app.route('/', methods = ["GET","POST"])
def add():
	num1 = int(request.args.get('val1'))
	num2 = int(request.args.get('val2'))
	res = num1 + num2
	res2 = num1 * num2
	return jsonify({'ans' : str(res),'ans2' : str(res2)})
	
@app.route('/select', methods = ["GET","POST"])
def select():
	return render_template('upload.html')	


	

@app.route('/retrive', methods = ['GET','POST'])
def retrive():	
	firebase1 = firebase.FirebaseApplication('https://friendlychat-3d8f7.firebaseio.com/imgPath/-L7SGb_ZY75OcivKMAxp', None)
	result = firebase1.get('/imgPath/-L7SGb_ZY75OcivKMAxp/photoUrl', None)
	# webbrowser.open(result)		
	r = requests.get(result, allow_redirects=True)
	open('google.jpeg', 'wb').write(r.content)
	return ("Image Downloaded")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8098, debug=True)
