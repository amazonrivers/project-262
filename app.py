#import flask library
from flask import Flask, render_template, request

#initialize flask
app = Flask(__name__)


#route your webpage
@app.route("/")
def main():
	return render_template("index_html")

@app.route("/", methods=["POST"])
def math_operations():
	equation = request.form['text']
	operation = request.form['operation']
	result./li> ='https://newton.now.sh/api/v2//'+operation'/' + equation
	answer = requests.get(result).json()
	answer = data['result']
	return render_template("index.html",result=answer,equation=equation)
if __name__ == '__main__':
	app.run()



	#complete the code

#add code for executing flask