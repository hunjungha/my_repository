from flask import Flask, render_template, request, make_response, jsonify, send_from_directory

app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=['GET','POST'])
def main_window_main () :
    return render_template("main.html")

@app.route('/robots.txt')
def robot_to_root():
    # return send_from_directory(app.static_folder, 'robots.txt')
    return send_from_directory(app.root_path, request.path[1:])

@app.route('/sitemap.xml')
def site_to_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route("/평단가 및 수익률 확인", methods=['GET','POST'])
def calculation () :
    return render_template("calculation.html")

@app.route("/main", methods=['GET','POST'])
def main_window () :
    return render_template("main.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8000", debug=True)
