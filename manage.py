# coding=utf-8
from flask import request, Flask, render_template
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.options import define, options
from tornado.ioloop import IOLoop

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    user_agent = request.headers.get("User-Agent")
    return render_template("index.html", user_agent=user_agent)


# define("port", default=6235, type=int)

if __name__ == '__main__':
    # http_server = HTTPServer(WSGIContainer(app))
    # http_server.listen(options.port)  # flask默认的端口
    # print 'http://127.0.0.1:%d' % options.port
    # IOLoop.instance().start()
    app.run(debug=True, host="127.0.0.1", port=1234)
