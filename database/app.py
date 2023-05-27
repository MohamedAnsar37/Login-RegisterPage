from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard_page():
    return render_template('dashboard.html')

'''@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the form
    username = request.form['username']
    password = request.form['password']

    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['Infos']
    users_collection = db['users']
    password_collection = db['password']

    # Query the "users" collection for the entered username
    user = users_collection.find_one({'username': username})

    if user:
        # User found, check the password from the "password" collection
        password_entry = password_collection.find_one({'username': username})

        if password_entry and password_entry['password'] == password:
            # Password matches, redirect to the dashboard or perform other actions
            return render_template('dashboard.html')
        else:
            # Password does not match, display an error message
            return render_template('login.html', error='Invalid credentials')
    else:
        # User not found, display an error message
        return render_template('login.html', error='Invalid credentials')
'''
if __name__ == '__main__':
    app.run(debug=True)
    client.close()
