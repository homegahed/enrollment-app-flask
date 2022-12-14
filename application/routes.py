from application import app
from application import db
from flask import render_template, request, redirect, json, Response
from application.forms import LoginForm, RegisterForm
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from application.dash1 import dash_app_1
from application.dash2 import dash_app_2

from application.models import User, Course, Enrollment



courses_data_dict = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, 
                    {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, 
                    {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, 
                    {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, 
                    {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"},
                    {"courseID":"6666","title":"Test2","description":"Test test test","credits":4,"term":"Summer"}]









@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template('index.html', index=True)


@app.route("/courses")
@app.route("/courses/<term>")
def courses(term="Fall 2019"):
    return render_template('courses.html', courses_data=courses_data_dict, courses=True, term=term)

@app.route("/register")
def register():
    return render_template('register.html', register=True)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', login=True, title='Login', form=form)


@app.route("/enrollment", methods=['GET', 'POST'])
def enrollment():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    
    return render_template('enrollment.html', enrollment=True,
                           data={"id":id, "title":title, "term":term})
    

@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if idx == None:
        jdata=courses_data_dict
    else:
        jdata = courses_data_dict[int(idx)]
        
    return Response(json.dumps(jdata), mimetype='application/json')




    
    
@app.route("/user", methods=['GET'])
def user():
    # User(user_id=1, first_name="Christian", last_name="Hur", 
    #      email="Christian@uta.com", password="password123").save()
    # User(user_id=2, first_name="Mary", last_name="Jane", 
    #      email="Mary@uta.com", password="password123").save()
    # User(user_id=3, first_name="Hossam", last_name="Megahed", 
    #      email="Hossam@uta.com", password="password123").save()
    users = User.objects.all()
    return render_template("user.html", users=users, user=True)




@app.route('/dash1/')
def dashboard1():
    return redirect('/dash1')


@app.route('/dash2/')
def dashboard2():
    return redirect('/dash2')






flask_dash = DispatcherMiddleware(app, {
    '/dash1':dash_app_1.server,
    '/dash2':dash_app_2.server
    })






    