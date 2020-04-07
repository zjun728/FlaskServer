from flask import render_template,request

from apps import app

@app.route('/',methods=["GET","POST"])
def index():
    if request.method=="POST":
        fs=request.files["image_upload"]
        if fs.filename!="":
            fs.save(fs.filename)
            return render_template('index.html',msg="上传成功")
    return render_template('index.html')