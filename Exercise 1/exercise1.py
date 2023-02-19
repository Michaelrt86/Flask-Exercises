from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/get')
def testMethod():
    TodayDate = datetime.datetime.now()
    thisYear = TodayDate.strftime("%Y")
    thisMonth = TodayDate.strftime("%B")
    thisWeekDay = TodayDate.strftime("%A")
    thisDay = TodayDate.strftime("%d")
    thisHour = TodayDate.strftime("%H")
    thisMin = TodayDate.strftime("%M")
    thisSec = TodayDate.strftime("%S")
    date = 'The current date time is ' + thisWeekDay + ', ' + thisMonth + ' ' + thisDay + ' ' + thisYear + ' ' + thisHour + ' ' + thisMin + ' ' + thisSec
    return render_template('get.html', htmlDate = date)


if __name__ == '__main__':
    app.run()