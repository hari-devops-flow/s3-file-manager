from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from werkzeug.utils import secure_filename
import boto3
import os
from io import BytesIO
from config import *

app = Flask(__name__)
app.secret_key = SECRET_KEY

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# Dummy login for demo
USERNAME = "admin"
PASSWORD = "password"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            return redirect(url_for('dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # Upload
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            s3.upload_fileobj(file, S3_BUCKET_NAME, filename)
            flash(f"Uploaded {filename} to S3")

    # List files
    objects = s3.list_objects_v2(Bucket=S3_BUCKET_NAME)
    files = [obj['Key'] for obj in objects.get('Contents', [])]

    return render_template('dashboard.html', files=files)


@app.route('/download/<filename>')
def download_file(filename):
    file_obj = BytesIO()
    s3.download_fileobj(S3_BUCKET_NAME, filename, file_obj)
    file_obj.seek(0)
    return send_file(file_obj, as_attachment=True, download_name=filename)


if __name__ == '__main__':
    app.run(debug=True)
