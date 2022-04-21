from flask import Flask, redirect, url_for, render_template,request,session

app = Flask(__name__)
app.config["SECRET_KEY"]="PhamTrungNghia"

@app.route('/home')
def Home():
    return render_template('home.html')

@app.route('/login',methods=["POST","GET"])
def Login():
    if request.method =="POST":
        user_name = request.form["name"]
        if user_name:
            session['user'] = user_name
            return redirect(url_for("hello_user",name = user_name))
    if 'user' in session:
        name = session['user']
        return f'<h1>Hello {name}!</h1>'
    return render_template('login.html')

@app.route('/user')
def hello_user():
    if 'user' in session:
        name = session['user']
        return f'<h1>Hello {name}!</h1>'
    else:
        return redirect(url_for('Login'))

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('Login'))

if __name__ == "__main__":
    app.run(debug=True)