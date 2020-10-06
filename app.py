from flask import Flask, render_template
from db import DataBase

def __init__(self):
    self.data = DataBase.__init__()


app = Flask(__name__)

@app.route('/cpu-load')
@app.route('/cpu-load/')

def load_show_last_10():
    history = DataBase.get_last()
    return render_template('load-history.html',
                            history=history,
                            length=len(history))

def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.debug = True
    app.run()
