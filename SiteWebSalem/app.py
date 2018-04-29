from doctest import debug
import sqlite3
from mock import Post

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('page_html/page_principale.html')


@app.route('/contact')
def contact():
    return render_template('page_html/page_contact.html')


@app.route('/contenu')
def contenu():
    return render_template('page_html/page_contenu.html')


@app.route('/secondaire')
def secondaire():
    return render_template('page_html/page_secondaire.html')


@app.route('/blog')
def post_index():
    list_post = Post.all()
    return render_template('post/index.html', post=list_post)


@app.route('/blog/post/<int:id>')
def post_show(id):
    list_post = Post.find(id)
    return render_template('post/show.html', post=list_post)


def page_not_found(error):
    return render_template('error/error_404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=3000)
