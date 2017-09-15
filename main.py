from flask import Flask, render_template, request, make_response, jsonify
import transform

app = Flask(__name__)

convert = transform.transform(True)

@app.route("/")
def home(name=None):
	return render_template('home.html', name=name)


@app.route("/transform", methods=['GET','POST'])
def render_json():
	# 
	if request.method == 'POST':
		try:
			firebase_json = convert.render(request.form.get('json'))
		except TypeError:
			print 'Error'

		return ("<pre>" + firebase_json + "</pre>")
	if request.method == 'GET':
		return "TEST"

if __name__ == "__main__":
	app.run(debug=True)