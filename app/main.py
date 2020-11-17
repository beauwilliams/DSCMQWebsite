from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("/index.html")


@app.route("/index.html")
def index():
    return render_template("/index.html")

@app.route("/code-of-conduct.html")
def codeOfConduct():
    return render_template("code-of-conduct.html")

# BEAU 17/11/20 -> Removed. No team page currently. #####TODO####
# @app.route("/team.html")
# def about():
#     return render_template("team.html")


@app.route("/events.html")
def events():
    return render_template("events.html")


if __name__ == "__main__":
    app.run(debug=True)
