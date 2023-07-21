from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
	return render_template("index.html")

@app.route("/experimental-writing/blank-work")
def blank_work():
	return render_template("blank.html")

@app.route("/poem/sonnet0")
def sonnet0():
	return render_template("sonnet0.html")

@app.route("/poem/sonnet47")
def sonnet47():
	return render_template("sonnet47.html")

if __name__ == "__main__":
	app.run()