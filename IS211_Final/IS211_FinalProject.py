from flask import Flask
from flask import render_template
from flask import request, redirect, url_for


app = Flask(__name__)

oldposts = [
    "Greetings: Welcome to my blog!| By: Amber| Posted on: January 2nd", 
    "Instructions: Feel free to post your thoughts| By: Amber| Posted on: January 4th"
]

blogposts= [
    "Introduction: My name is Jennifer| By:Jennifer|Posted on: January 6th"
]

@app.route('/')
def home():
    print(oldposts)
    print(blogposts)
    return redirect(url_for("blog"))
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        if (username == 'user' and password == 'apple'):
            return redirect(url_for("posts")) 
        else:
            return redirect(url_for('login'))
    return render_template('login.html') 
    
 
@app.route('/blog', methods=['POST', 'GET'])
def blog(): 
    print(oldposts)
    print(blogposts)
    return render_template('blog.html', oldposts= oldposts, blogposts=blogposts)
 
@app.route('/dashboard',methods = ['POST', 'GET'])
def posts():
    if request.method == 'POST':
        print(oldposts)
        blog = request.form['blogpost'] 
        blogposts.append(blog)
        print(blogposts)
        return redirect(url_for("posts"))
    return render_template('dashboard.html', blogposts=blogposts)

@app.route('/editblog', methods = ['POST', 'GET'])
def edit():
    if request.method == 'POST':
        
        editpost= request.form['blogpost']
        edits= request.form['edits']
        newedit= editpost.update(edits)
        print(newedit)
        
    return render_template('dashboard.html', blogposts=blogposts)

@app.route('/delete', methods = ['POST', 'GET'] )
def delete():
    selectpost = request.form['blogpost']
    selectpost.delete()
    return redirect(url_for('posts'))
if __name__ == "__main__":
    app.run(debug=True)
