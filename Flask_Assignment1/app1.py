from flask import Flask, render_template
import mysql.connector


from db_config import db_config
from flask import Flask, render_template, request, redirect, url_for

# Connect to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor(dictionary=True)
app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

# Profile page route
@app.route('/profile')
def profile():
    return render_template('profile.html')

# Contact page route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# ------------------ Blog CRUD Routes ------------------

from flask import request, redirect, url_for, render_template

# List all posts
@app.route('/blog')
def blog():
    cursor.execute("SELECT * FROM posts ORDER BY created_at DESC")
    posts = cursor.fetchall()
    return render_template('blog.html', posts=posts)

# Create a new post
@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
        conn.commit()
        return redirect(url_for('blog'))
    return render_template('create_post.html')

# View a single post
@app.route('/view_post/<int:post_id>')
def view_post(post_id):
    cursor.execute("SELECT * FROM posts WHERE id=%s", (post_id,))
    post = cursor.fetchone()
    return render_template('view_post.html', post=post)

# Edit a post
@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    cursor.execute("SELECT * FROM posts WHERE id=%s", (post_id,))
    post = cursor.fetchone()
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        cursor.execute("UPDATE posts SET title=%s, content=%s WHERE id=%s", (title, content, post_id))
        conn.commit()
        return redirect(url_for('blog'))
    return render_template('edit_post.html', post=post)

# Delete a post
@app.route('/delete_post/<int:post_id>')
def delete_post(post_id):
    cursor.execute("DELETE FROM posts WHERE id=%s", (post_id,))
    conn.commit()
    return redirect(url_for('blog'))

if __name__ == '__main__':
    app.run(debug=True)