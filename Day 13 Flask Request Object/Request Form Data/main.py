from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def customer():
    if request.method =='POST':
        data = request.form
        return render_template('success.html',data = data )
    return render_template('customer.html')       




if __name__ == '__main__':
    app.run(debug=True)