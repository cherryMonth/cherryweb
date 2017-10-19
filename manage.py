# coding=utf-8
from flask import request, Flask, render_template
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.options import define, options
from tornado.ioloop import IOLoop
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)

bootstrap = Bootstrap(app)  # 用bootstrap初始化app
moment = Moment(app)  # 用Moment初始化app 获取本地时间


@app.errorhandler(404)
def page_not_found():
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", current_time=datetime.datetime.utcnow())


define("port", default=1234, type=int)

if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(options.port)  # flask默认的端口
    print 'http://127.0.0.1:%d' % options.port
    IOLoop.instance().start()
