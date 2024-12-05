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
        return "No file provided"

@app.route("/", methods=["GET"])
def form():
    return '''
    <!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Upload New File</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
    }
    form {
      display: flex;
      flex-direction: column;
      gap: 15px;
    }
    label {
      font-weight: bold;
    }
    input[type="submit"] {
      padding: 10px;
      background-color: #007BFF;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    input[type="submit"]:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <h1>Upload a New File</h1>
  <form method="post" enctype="multipart/form-data">
    <div>
      <label for="file">Zip file with stats:</label>
      <input type="file" id="file" name="file" required>
    </div>
    <div>
      <label for="measurement">Measurement (name of table in DB)</label>
      <input type="text" id="measurement" name="measurement" placeholder="e.g., Gateway1" required>
    </div>
    <div>
      <input type="submit" value="Upload">
    </div>
  </form>
</body>
</html>
    '''


if __name__ == "__main__":
    app.secret_key = 'secret key'
    app.run()
