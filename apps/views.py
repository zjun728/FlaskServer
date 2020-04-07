import os

from flask import render_template,request

from apps import app

@app.route('/',methods=["GET","POST"])
def index():
    if request.method=="POST":
        fs=request.files["image_upload"]
        print(fs.filename)
        if fs.filename!="":
            file_path=os.path.join(app.config["ABS_UPLOAD_FOLDER"],fs.filename)
            print(file_path)
            fs.save(file_path)
            return render_template('index.html',msg="上传成功")
    return render_template('index.html')