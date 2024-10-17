#first build a simple flask server

from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def home():
#     return "hello world!"
#
#
# if __name__ == '__main__':
#     app.run()

#how can we render an HTML webpage crafted inside an HTML file rather than just returning a string like above?
#create an html file in pycharm

from flask import render_template

@app.route('/')
def home():
    return render_template("index.html")       #use th file path if in a sub folder in the templates folder


@app.route('/resume')
def resume():
    return render_template("resume.html")


if __name__ == '__main__':
    app.run(debug=True)

# This renders the html and displays the webpage, however, without any static files(images), unless they are moved to the static folder




