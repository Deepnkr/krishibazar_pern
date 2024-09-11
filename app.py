from flask import Flask, render_template, request, session, url_for, redirect
import psycopg2

app = Flask(__name__)
app.secret_key = 'skey'



# DB
conn = psycopg2.connect('postgresql://postgres:1234@localhost/krishibazar')

@app.route('/addproduct', methods=['GET', 'POST'])
def addProduct():
    if request.method == "GET":
        if 'user' in session and session['email'] == 'admin@krishi.com':
            return render_template('pages/addproduct.html')
        else:
            return "error"
    elif request.method == "POST":
        if 'user' in session and session['email'] == 'admin@krishi.com':
            name = request.form['product-name']
            description = request.form['product-description']
            price = request.form['product-price']
            image = request.form['product-image']
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO products (name, description, price, image_url) VALUES (%s, %s, %s, %s)",
                (name, description, price, image)
            )
            conn.commit()
            return "Success"

# Routes
@app.route('/')
def home():
    cur = conn.cursor()
    cur.execute('SELECT * FROM products LIMIT 4')  # Fetch a limited number of products
    products = cur.fetchall()
    return render_template('pages/home.html', products=products)

@app.route('/products')
def products():
    cur = conn.cursor()
    cur.execute('SELECT * FROM products')
    rows = cur.fetchall()
    return render_template('pages/products.html', rows=rows)

@app.route('/add_review', methods=['POST'])
def add_review():
    try:
        name = request.form['name']
        rating = request.form['rating']
        review = request.form['review']
        product_id = request.form['product_id']  # Fetch product_id from hidden input field

        # Insert the review into the database
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO reviews (product_id, name, rating, review) VALUES (%s, %s, %s, %s)',
            (product_id, name, rating, review)
        )
        conn.commit()

        # Redirect back to the product details page
        return redirect(f'/product/{product_id}')
    except KeyError as e:
        return f"Missing form field: {str(e)}", 400


@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/contacts')
def contacts():
    return render_template('pages/contacts.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'user' in session:
            return render_template('pages/profile.html')
        return render_template('pages/login.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE email=%s', (email,))
        user = cur.fetchone()
        if user and user[2] == password:
            session['user'] = user[0]
            session['email'] = user[3]
            return render_template('pages/profile.html')
        else:
            return "Error:"

@app.route('/logout', methods=['POST'])
def logout():
    if request.method == 'POST':
        session.pop('user')
        return redirect('/')

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    cur = conn.cursor()
    
    # Fetch the product details
    cur.execute('SELECT * FROM products WHERE id = %s', (product_id,))
    product = cur.fetchone()

    # Fetch the reviews for this product
    cur.execute('SELECT name, rating, review, created_at FROM reviews WHERE product_id = %s ORDER BY created_at DESC', (product_id,))
    reviews = cur.fetchall()

    return render_template('pages/product_detail.html', product=product, reviews=reviews)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        if 'user' in session:
            return render_template('pages/profile.html')
        return render_template('pages/signup.html')
    elif request.method == 'POST':
        fname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        cur = conn.cursor()
        if password != cpassword:
            return "Error: Passwords do not match"
        else:
            try:
                cur.execute(
                    'INSERT INTO users (fname, email, password) VALUES (%s, %s, %s)',
                    (fname, email, password)
                )
                conn.commit()
                return redirect('/login')
            except Exception as e:
                return f"Error: {e}"

#Add to cart
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # Get the product ID from the form
    product_id = request.form['product_id']

    # Initialize the cart in the session if it doesn't exist
    if 'cart' not in session:
        session['cart'] = []

    # Check if the product is already in the cart
    if product_id not in session['cart']:
        session['cart'].append(product_id)

    # Redirect to the product page or cart page
    return redirect('/cart')


#App rout
@app.route('/cart')
def cart():
    if 'cart' not in session or len(session['cart']) == 0:
        return "Your cart is empty."

    # Fetch the products from the database based on product IDs in the cart
    cur = conn.cursor()
    cur.execute('SELECT * FROM products WHERE id IN %s', (tuple(session['cart']),))
    cart_items = cur.fetchall()

    # Render the cart page with the cart items
    return render_template('pages/cart.html', cart_items=cart_items)


#remove cart
@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    product_id = request.form['product_id']  # Product ID from form (string)
    
    # Convert product_id to string to ensure it matches the session's product_id format
    if 'cart' in session:
        # Ensure product_id is a string before removing
        cart = session['cart']
        if str(product_id) in cart:
            print(f"Removing product_id: {product_id} from cart")
            cart.remove(str(product_id))  # Remove the product from the cart
        else:
            print(f"Product ID {product_id} not found in cart")

    return redirect('/cart')


if __name__ == '__main__':
    app.run(port=3000, debug=True)
