from flask import Flask,render_template,redirect,request
import numpy as np
import caption_it
app = Flask(__name__)  # module name

@app.route('/')
def hello():
    return render_template("index.html") 

@app.route('/', methods = ['POST'])
def main():
    if request.method == 'POST':
        f=request.files['userfile']
        path='./static/{}'.format(f.filename)  # saves the file in static folder
        f.save(path)
        
        caption = caption_it.caption_this(path)
        result_dic = {
            'image':path,
            'caption':caption
        }
        
    return render_template("index.html",your_result = result_dic) 

if __name__  == '__main__':
    app.run(debug=True)