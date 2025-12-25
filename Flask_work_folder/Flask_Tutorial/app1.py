from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',user="Priya")


@app.route('/contact')
def contact():
    return render_template('contact.html',email='support@itdefined.com',phone='+91 1234567890')

@app.route('/about')
def about():
     details ={
         'emails':'support@itdefined.org',
         'phone' :'+91 1234567890',
         'courses':['MERN','Django','Devops','Embeded']
     }

     return render_template('about.html',details=details)


# @app.route('/register')
# def register():
#     return render_template('register.html')


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        details = { "name" : request.form.get('name'),
                    "email" : request.form.get('email'),
                    "password" : request.form.get('pwd') }

        return details
    else:
        return render_template('register.html')



# @app.route('/registration', methods=['POST'])
# def registration():
    # print("====>",request.args)
    # details = { "name" : request.form.get('name'),
    #             "email" : request.form.get('email'),
    #             "password" : request.form.get('pwd') }

    # return details

# app.run(debug=True,port='5001')

app.run(debug=True)