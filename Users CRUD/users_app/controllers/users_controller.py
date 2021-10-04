from os import X_OK
from flask import render_template, redirect, request
from users_app import app
from users_app.models.user import User
#===========================================================================================================

@app.route ('/users/new', methods=['GET'])
def createpage():
    return render_template ('create.html')

@app.route ('/users', methods=['GET'])
def users_page():
    users = User.get_users_info()

    return render_template ('read.html', users = users)
    
#===========================================================================================================
@app.route ('/users/new', methods=['POST'])
def addNew():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    newUser = (first_name,last_name,email)
    User.addUser(newUser)
    return redirect('/users')
#===========================================================================================================
@app.route ('/users/<int:id>', methods=['GET'])
def show (id):
    data = id
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    userNewInfo = (first_name,last_name,email)
    info = User.showUserInfo(data)

    return render_template ('info.html', userinfo = info)




#===========================================================================================================
@app.route ('/users/<int:id>/edit', methods=['GET'])
def displayUserInfo(id):
    data = id
    info = User.showUserInfo(data)
    return render_template('edit.html', user = info)

@app.route ('/users/update', methods=['POST'])
def editUserInfo():
    user_id = request.form['user_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    userNewInfo = (user_id,first_name,last_name,email)
    print(userNewInfo)
    User.editUser(userNewInfo)

    return redirect('/users')



#===========================================================================================================

@app.route ('/users/<int:id>/delete', methods=['GET'])
def deleteusr(id):
    user_id = {
        "id" : id
    }
    User.deleteuser(user_id)
    return redirect('/users')
    
