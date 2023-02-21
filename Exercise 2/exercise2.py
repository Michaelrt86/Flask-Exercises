from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
#Zoey Vail helped me on this assignment
@app.route("/")
def submit():
        return render_template('form.html')
@app.route("/calculate",methods=["POST"])
def calculate():
    if request.method == 'POST':
        try:
            userResponse = int(request.form.get('number'))
            if userResponse % 2 == 0:
                temp = str(userResponse) + ' is even'
            else:
                temp = str(userResponse) + ' is even'
        except Exception:
            temp = 'Invalid input'
        return render_template('calculate.html', temp2 = temp)
    

if __name__ == '__main__':
    app.run(debug=True)