from flask import Flask, render_template, request, make_response, jsonify

app = Flask(__name__)


@app.route("/평단가 및 수익률 확인", methods=['GET','POST'])
def calculation () :
    return render_template("calculation.html")

@app.route("/main", methods=['GET','POST'])
def main_window () :
    return render_template("main.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")



