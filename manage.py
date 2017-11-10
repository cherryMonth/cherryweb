# coding=utf-8
from flask import request, Flask, render_template, session, redirect, url_for, flash
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.options import define, options
from tornado.ioloop import IOLoop
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
import datetime
from flask.ext.wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)  # 用bootstrap初始化app
moment = Moment(app)  # 用Moment初始化app 获取本地时间


class NameForm(FlaskForm):
    name = StringField("what is your name!", validators=[Required()])
    submit = SubmitField("Submit")


@app.errorhandler(404)
def page_not_found():
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


@app.route("/love")
def love():
    return render_template("love.html")


@app.route("/birthday")
def birthday():
    return render_template("birthday.html")


@app.route("/", methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old = session.get('name')
        if old is not None and old != form.name.data:
            flash('look like  you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template("index.html", current_time=datetime.datetime.utcnow(), form=form, name=session.get('name'))



define("port", default=1234, type=int)

if __name__ == '__main__':
    #pid = os.getpid()
    #filename = open("/root/cherryweb/pid.txt","w")
    #filename.write(str(pid))
    #filename.close()
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(options.port)  # flask默认的端口
    print 'http://127.0.0.1:%d' % options.port
    IOLoop.instance().start()
