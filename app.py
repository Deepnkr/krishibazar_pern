from flask import Flask, render_template,request,session,redirect
import psycopg2

app=Flask(__name__)
app.secret_key = 'skey'

# DB
conn = psycopg2.connect('postgresql://postgres:1234@localhost/krishibazar')

# Routes
@app.route('/')
def home():
    return render_template('pages/home.html') 



@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        if 'user' in session:
           return render_template('pages/profile.html')
        return render_template('pages/login.html')
    elif request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        cur=conn.cursor()
        cur.execute('SELECT * FROM users WHERE email=%s',(email,))
        user=cur.fetchone()
        if user and user[2]==password:
            session['user']=user[0]
            return render_template('pages/profile.html')
        else:
            return "Error:"

@app.route('/logout',methods=['POST'])
def logout():
    if request.method == 'POST':
        session.pop('user')
        return redirect('/')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        if 'user' in session:
           return render_template('pages/profile.html')
        return render_template('pages/signup.html')
    elif request.method == 'POST':
        fname = request.form['fullname']
        email=request.form['email']
        password=request.form['password']
        cpassword=request.form['cpassword']
        cur=conn.cursor()
        if password != cpassword:
            return "Error: Passwords do not match"
            
        else:
            try:
                cur = conn.cursor()
                cur.execute(
                    'INSERT INTO users (fname, email, password) VALUES (%s, %s, %s)',
                    (fname, email, password)
                )
                conn.commit()
                return redirect('/login')
            except:
                return "Error "
    

if __name__ == '__main__':
    app.run(port=3000,debug=True)