from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/get')
def testMethod():
    return render_template('submit.html')

@app.route('/submit', methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        user = request.form["Number"]
        return redirect(url_for("user", usr = user))
    else:
        return render_template('submit.html')
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"
if __name__ == '__main__':
    app.run()