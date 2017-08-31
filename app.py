from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
@app.route("/")
def home():
	return render_template("home.html")

@app.route("/login", methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('home'))
	return ''' <form action = "" method = "post">
      <p><input type = text name = username /></p>
      <p><input type = submit value = Login /></p>
   </form>
	
   '''


if __name__ == '__main__':
	app.run("0.0.0.0", 5000, debug = True)