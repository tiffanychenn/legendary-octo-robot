from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
	return render_template("index.html")

@app.route("/experimental-writing/blank-work")
def blank_work():
	return render_template("blank.html")

if __name__ == "__main__":
	app.run()