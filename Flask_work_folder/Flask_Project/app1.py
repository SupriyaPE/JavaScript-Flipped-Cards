# from flask import Flask
# from flask_mysqldb import MySQL

# app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '9019860150' 
# app.config['MYSQL_DB'] = 'flask_blog'

# mysql = MySQL(app)

# @app.route('/')
# def home():
#     return "MySQL connected successfully!"

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '9019860150' 
app.config['MYSQL_DB'] = 'flask_blog'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM posts")
    posts = cur.fetchall()
    cur.close()
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO posts (title, body) VALUES (%s, %s)", (title, body))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))

    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/view/<int:id>')
def view(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM posts WHERE id=%s", (id,))
    post = cur.fetchone()
    cur.close()
    return render_template('view.html', post=post)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM posts WHERE id=%s", (id,))
    post = cur.fetchone()

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        cur.execute("UPDATE posts SET title=%s, body=%s WHERE id=%s", (title, body, id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('view', id=id))

    cur.close()
    return render_template('edit.html', post=post)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM posts WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))