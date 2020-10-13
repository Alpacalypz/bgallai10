# Team Glasses -- *Benjamin Gallai, Jason Chan, William Li
# SoftDev -- Rona Ed.
# K10 -- Putting Little Pieces Together/Flask Intro/Send output of occupation chooser to webpage
# 2020-10-13

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

#no change from v3. if app.py is imported like a library, you don't want it to run (you just need the variables and functions it defines), so don't do app.run(), or change app.debug
