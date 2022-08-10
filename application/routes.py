
from application import app
from application import db
from flask import render_template, request, redirect




from dash import Dash

from dash import Output, Input

from werkzeug.middleware.dispatcher import DispatcherMiddleware
# from application.dash1 import d1
from application.dash2 import d2


from application.dsh1 import dash_app_1










@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template('index.html', index=True)


@app.route("/courses")
@app.route("/courses/<term>")
def courses(term="Fall 2019"):
    
    courses_data_dict = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, 
                         {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, 
                         {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, 
                         {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, 
                         {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"},
                         {"courseID":"6666","title":"Test2","description":"Test test test","credits":4,"term":"Summer"}]

    # print(courses_data_dict[0])
    return render_template('courses.html', courses_data=courses_data_dict, courses=True, term=term)

@app.route("/register")
def register():
    return render_template('register.html', register=True)


@app.route("/login")
def login():
    return render_template('login.html', login=True)


@app.route("/enrollment", methods=['GET', 'POST'])
def enrollment():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    
    return render_template('enrollment.html', enrollment=True,
                           data={"id":id, "title":title, "term":term})
    



class User(db.Document):
    user_id     =    db.IntField( unique= True )
    first_name  =    db.StringField( max_length=50 )
    last_name   =    db.StringField( max_length=50 )
    email       =    db.StringField( max_length=30 )
    password    =    db.StringField( max_length=30 )
    
    
@app.route("/user", methods=['GET'])
def user():
    # User(user_id=1, first_name="Christian", last_name="Hur", 
    #      email="Christian@uta.com", password="password123").save()
    # User(user_id=2, first_name="Mary", last_name="Jane", 
    #      email="Mary@uta.com", password="password123").save()
    # User(user_id=3, first_name="Hossam", last_name="Megahed", 
    #      email="Hossam@uta.com", password="password123").save()
    users = User.objects.all()
    return render_template("user.html", users=users)




@app.route('/dsh_1/')
def dashboard1():
    return redirect('/dsh_1')





flask_dash = DispatcherMiddleware(app, {
    '/dsh_1':dash_app_1.server
    })

# @app.route('/dsh_1/')
# def d():
#     return redirect('/dsh_1')





    