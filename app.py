from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
	return render_template("index.html")

@app.route("/experimental-writing/blank-work")
def blank_work():
	return render_template("blank.html")

@app.route("/experimental-writing/changed-work")
def changed_work():
	with open('/var/www/legendary-octo-robot/static/pride-and-prejudice.txt', 'r') as f:
		return f.read().replace("\n", "<br>")

if __name__ == "__main__":
	app.run()