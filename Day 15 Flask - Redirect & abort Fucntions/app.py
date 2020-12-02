from flask import Flask, render_template,request, url_for, redirect, abort
app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def login():
    if request.method =='POST':
        if request.form['email']=='admin@seferyak.com' and request.form['password']=='admin':
            return redirect(url_for('success'))
        else:
            abort(401)
    return render_template ('login.html')

@app.route('/success')
def success():
    return f"You have logged in succesfully!"

if __name__ == '__main__':
    app.run(debug=True)