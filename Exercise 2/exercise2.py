from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr = user))
    else:
        return render_template('form.html')
@app.route("/<usr>")
def user(usr):
    try:
        userResponse = int(usr)
        if userResponse % 2 == 0:
            return render_template("calculate.html", number = userResponse,state = "even")
        else:
            return f"<h1>The number is odd</h1>"
    except Exception:
        return render_template("form.html")
    

if __name__ == '__main__':
    app.run()