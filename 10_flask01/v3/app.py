# Team Glasses -- *Benjamin Gallai, Jason Chan, William Li
# SoftDev -- Rona Ed.
# K10 -- Putting Little Pieces Together/Flask Intro/Send output of occupation chooser to webpage
# 2020-10-13

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True #when app.py is edited and saved, the terminal says change detected, and refreshes the page. 
app.run()
