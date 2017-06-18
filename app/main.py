from flask import Flask, send_file, send_from_directory
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World from Flask"

@app.route("/")
def main():
    return send_file('./static/index.html')

@app.route('/node_modules/<path:path>')
def send_vendor_js(path):
    return send_from_directory('static/node_modules', path)

@app.route('/scripts/<path:path>')
def send_js(path):
    return send_from_directory('static/scripts', path)

@app.route('/style/<path:path>')
def send_style(path):
    return send_from_directory('static/style', path)

@app.route('/templates/<path:path>')
def send_template(path):
    return send_from_directory('static/templates','.'.join([path,'html']))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
