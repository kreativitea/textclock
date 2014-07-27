import json
from flask import Flask, render_template

import TextClock


app = Flask(__name__)
app.config.from_object(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/')
def hello():
    return render_template('index.html',
                           clockface=TextClock.face,
                           textclock=list(TextClock.render()))


@app.route('/update')
def reload():
    return json.dumps(list(TextClock.render()))
    

if __name__ == '__main__':
    app.debug = True
    app.run()
