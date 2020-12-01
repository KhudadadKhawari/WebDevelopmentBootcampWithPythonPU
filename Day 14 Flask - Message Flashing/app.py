from flask import Flask, render_template, flash, request, redirect, url_for
app = Flask(__name__)
app.config['SECRET_KEY'] ='ASDKksdfk'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method =='POST':
        if request.form['email'] == 'admin@seferyak.com' and request.form['password'] == 'admin':
            flash('You Have Logged in Successfully')
            return redirect(url_for('index'))
        else:
            flash('EMail or Password is Incorrect')
            return redirect(url_for('login'))

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)