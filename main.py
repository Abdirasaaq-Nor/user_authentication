from flask import  Flask, render_template,request,redirect,url_for

app = Flask(__name__)


@app.route('/')
@app.route('/singup')
@app.route('/register')
def sing_up():
    return render_template('register.html')



@app.route('/singin')
@app.route('/login')
def login():
    return render_template('login.html')




@app.route('/forget_passowrd')
def forget_passowrd():
    return render_template('forget_passwod.html')




@app.route('/home')
def home():
    return render_template('home.html')




@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run(debug=True)