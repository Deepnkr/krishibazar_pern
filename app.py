from flask import Flask, render_template,request,session,redirect
import psycopg2

app=Flask(__name__)
app.secret_key = 'skey'

# DB
conn = psycopg2.connect('postgresql://postgres:1234@localhost/krishibazar')
@app.route('/addproduct',methods=['GET','POST'])
def addProduct():
    if request.method=="GET":
        if 'user' in session and session['email'] == 'admin@krishi.com':
            return render_template('pages/addproduct.html')
        else:
            return "error"
    elif request.method=="POST":
         if 'user' in session and session['email'] == 'admin@krishi.com':
            name=request.form['product-name']
            description=request.form['product-description']
            price=request.form['product-price']
            image=request.form['product-image']
            cur=conn.cursor()
            cur.execute("INSERT INTO products(name,description,price,image_url) VALUES('"+name+"','"+description+"',"+price+",'"+image+"')")
            conn.commit()
            return "Sucess"
# Routes
@app.route('/')
def home():
    return render_template('pages/home.html') 

@app.route('/products')
def products():
    cur=conn.cursor()
    cur.execute('SELECT * FROM products')
    rows=cur.fetchall()
  
    return render_template('pages/products.html',rows=rows) 

@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/contacts')
def contacts():
    return render_template('pages/contacts.html')
    


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
            session['email']=user[3]
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