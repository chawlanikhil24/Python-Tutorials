from flask import Flask, request, url_for, render_template
#Imported 4 very basic necessary modules to build a flask app

#Flask - to register the flask and deploy it on a local server
#request - to handle the incoming, GET,POST,PUT,DELETE request
#url_for -  to locate static files (css,js) on server
#render_template - to fetch the required HTML template at the corresponding url

#NOOTE: INCASE, OUR APP IS ONLY BACKEND-BASED, that is no, front-end is required then, Use only "Flask" & "request"

import json

#STEP 1: initiate your app
app = Flask(__name__)

#STEP 2: now, setup your routing URLs. ROUTING URLS, are URL patterns on which diffent operations of the app performs.
@app.route("/")# "/", that means we are setting up the HOME PAGE , what will occur on the landing on the home page.
def home(): #Now were defining the function, which will run on landing on the home page
    return json.dumps({"status":"1","message":"You are successfully landed on the home page"})

@app.route("/url2",methods=["GET"]) #I can specify that, which request method to be used for this particular URL
def url2():
    return json.dumps({"status":"1","message":"Successfully landed on url2 which is accepts only GET requests"})

@app.route("/url3",methods=["POST"])
def url3():
    return json.dumps({"status":"1","message":"Successfully landed on url3 which is accepts only POST requests"})
    #if you see "METHOD NOT ALLOWED" on browser, then don;t woryy, because, browser only makes GET requests by default

@app.route("/url4",methods=["GET","POST"])
def url4():
    if request.method == "GET":
        return json.dumps({"status":"1","message":"Successfully landed on url4 which is accepts both requests, but NOW your made a GET request"})
    else:
        return json.dumps({"status":"1","message":"Successfully landed on url4 which is accepts both requests, but NOW your made a POST request"})

#STEP 3: Now, since I've setted up my routing URLS, now its the time to run the app
#Don't Panic, No more steps, this is the last one

if __name__ == '__main__':
    app.run(debug=True) #run the app, debug is TRUE in development mode, so that any error while developing the error can be solved
