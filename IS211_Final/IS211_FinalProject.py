from flask import Flask
from flask import render_template
from flask import request, redirect, url_for


app = Flask(__name__)

blogposts= []

@app.route('/')
def home():
    return redirect(url_for("blog"))
    
@app.route('/dashboard')
def posts():
    return redirect(url_for("blog"))

@app.route('/blog', methods = ['POST', 'GET'])
def createblog():
    return render_template('blog.html', blogposts=blogposts)

@app.route('/addtoblog', methods=['POST', 'GET'])
def blog():
    if request.method == 'POST':
        blog = request.form['blog']
        blogposts.append(blog)
        print(blogposts)
        return render_template('blog.html', blogposts=blogposts)



if __name__ == "__main__":
    app.run(debug=True)
