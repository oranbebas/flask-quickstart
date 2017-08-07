from flask import Flask, url_for, render_template, request
fromwerkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    return "Index Page"

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username']),
                        request.form['password']):
            return log_the user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

@app.route('/upload', methods=['GETS', 'POST'])
def upload_file():
    if request.method == 'POST'
    f = request.files['the_file']
    f.save('/var/www/uploads/' + secure_filename(f.filename))

@app.route('/user/<username>')
def profile(username):
    return render_template('hello.html', name=username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John'))
