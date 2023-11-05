from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql

sql_host = "localhost"
sql_user = "root"
sql_pass = "Ganesh*143"
sql_db = "django_website"

username = ''
email = ''
password = ''
c_password = ''

# Create your views here.
def signupAction(request):
    userData = ""
    global username, email, password, c_password
    web_response = "" 
    try:
        if request.method=="POST":
            mySql = sql.connect(host = sql_host, user = sql_user, passwd = sql_pass, database = sql_db)
            cursor = mySql.cursor()
            data = request.POST
            for key,value in data.items():
                if key=='username':
                    username = value
                if key=='email':
                    email = value
                if key=='password':
                    password = value
                if key=='c_password':
                    c_password = value  
            if(username != ''):
                if(email != ''):
                    if(password != ''):
                        if(c_password != ''):
                            if(password == c_password):
                                query = "insert into users Values('{}','{}','{}')".format(username,email,password)
                                cursor.execute(query)
                                userData = username
                            else:
                                web_response = "Passwords Do Not Match" 
                        else:
                            web_response = "Confirm Password Cannot Be Null" 
                    else:
                        web_response = "Password Cannot Be Null" 
                else:
                    web_response = "Email Cannot Be Null" 
            else:
                web_response = "Username Cannot Be Null"          
        mySql.commit()
    except:
        web_response = "There was some unknown error!"

    Dict = {
        'response': web_response,
        'name': userData
    }

    if(web_response != ""):
        return render(request, 'error.html', Dict)
    else:
        return render(request, 'welcomeUser.html', Dict)
        
def signinAction(request):
    userData = {}
    global email, password
    web_response = ""  
    try:
        if request.method=="POST":
            mySql = sql.connect(host = sql_host, user = sql_user, passwd = sql_pass, database = sql_db)
            cursor = mySql.cursor()
            data = request.POST
            for key,value in data.items():
                if key=='email':
                    email = value
                if key=='password':
                    password = value
            if(email != ''):
                if(password != ''):
                    query = "select * from users where Email='{}' and Password='{}'".format(email,password)
                    cursor.execute(query)
                    t = tuple(cursor.fetchall())
                    if(t!=()):
                        userData = {
                            'name': str(t[0][0])
                        }
                    else:
                        web_response = "User Account does not exist!" 
                else:
                    web_response = "Password Cannot Be Null" 
            else:
                web_response = "Email Cannot Be Null"          
    except:
        web_response = "There was some unknown error!"
        
    webResponseDict = {
        'response' : web_response
    }

    if(web_response != ""):
        return render(request, 'error.html', webResponseDict)
    else:
        return render(request, 'welcomeUser.html', userData)


