from flask  import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['POST'])  
def file_upload():  
    return render_template("file_upload.html")  

@app.route('/success', methods=['POST'])  
def success(): 
    if request.method == 'POST':
        new_file = request.files['file']
        new_file.save(new_file.filename)
        return render_template("success.html", fname = new_file.name)  

if __name__ == '__main__':
    app.run(debug= True)