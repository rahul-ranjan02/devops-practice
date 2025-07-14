from flask import Flask, request, render_template_string
import os, datetime

UPLOAD_DIR = '/uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Upload Log</title>
<h1>Upload a Log File</h1>
<form method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Upload>
</form>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        f = request.files['file']
        if f and f.filename:
            path = os.path.join(UPLOAD_DIR, f.filename)
            f.save(path)
            print(f"[{datetime.datetime.utcnow()}] saved {path}")
            return "✅ Uploaded and saved.<br><a href='/'>Back</a>"
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

