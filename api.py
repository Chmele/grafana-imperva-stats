"""
API backend, used for retrieving the zipfile with imperva logs
"""
from flask import Flask, request, redirect
from iozip import ImpervaLog
from client import write_points


app = Flask(__name__)


@app.route("/", methods=["POST"])
def process_log():
    try:
        plain = ImpervaLog(request.files['file']).flat_payload(request.form.get("measurement"))
        write_points(plain)
        return "Success"
    except (KeyError, AttributeError):
        return redirect(request.url)

@app.route("/", methods=["GET"])
def form():
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=text name=measurement>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == "__main__":
    app.secret_key = 'secret key'
    app.run()
