from flask import Flask
import os
from loguru import logger
from datetime import datetime
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def hello_world():
    logger.info("访问了")
    logger.info(f"当前时间{datetime.now()}")

    return "<p>Hello, World!</p>"



@app.route("/<name>")
def hello2(name):
    return f"Hello, {escape(name)}!"

@app.route('/hello')
def hello():
    return 'Hello, World'


from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'



if __name__ == '__main__':
    server_port = os.environ.get('PORT', '5001')
    app.run(debug=True, port=server_port, host='0.0.0.0')