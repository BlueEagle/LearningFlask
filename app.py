from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Collin Ballou',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January, 24 2020'
    },
    {
        'author': 'Collin Ballou',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January, 24 2020'
    }
]

@app.route("/")
@app.route('/home')
def index():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')