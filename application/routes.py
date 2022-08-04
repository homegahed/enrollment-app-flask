
from application import app
from flask import render_template, request



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