from flask import Flask
from flask import render_template
from flask import request, redirect, url_for


app = Flask(__name__)

oldposts = [
    {"Greetings, welcome to my blog!| By: Amber| Posted on: January 2nd"}, 
    {"Instructions: Feel free to post your thoughts| By: Amber| Posted on: January 4th"}
]

blogposts= [
 
]

@app.route('/')
def home():
    
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
    return render_template('blog.html', blogposts=blogposts)
 
@app.route('/dashboard',methods = ['POST', 'GET'])
def posts():
    if request.method == 'POST':
        print(oldposts)
        blog = request.values.get('blogpost') 
        blogposts.append({blog})
        print(blogposts)
        
    return render_template('dashboard.html', blogposts=blogposts)

@app.route('/editblog', methods = ['POST', 'GET'])
def edit():
    if request.method == 'POST':
        editpost=  request.values.get("blogpost")
        edits= request.values.get('edits')
        newedit= editpost.update(edits)
        print(newedit)
        
    return render_template('dashboard.html', blogposts=blogposts)

@app.route('/delete', methods = ['POST', 'GET'] )
def delete():
    if request.method == 'POST':
        selectpost =  request.values.get("blogpost")
        selectpost.delete()
    return render_template('dashboard.html', blogposts=blogposts)
if __name__ == "__main__":
    app.run(debug=True)
