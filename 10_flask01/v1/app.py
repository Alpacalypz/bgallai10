# Team Glasses -- *Benjamin Gallai, Jason Chan, William Li
# SoftDev -- Rona Ed.
# K10 -- Putting Little Pieces Together/Flask Intro/Send output of occupation chooser to webpage
# 2020-10-13

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    #no print(__name__), so __name__ is not printed in the terminal when the url is accessed.
    return "No hablo queso!"

app.run()

