from flask import Flask

app = Flask(__name__)
app.debug=True



import  apps.views      #只能放到最后，防止循环引用



