from flask import Flask
from flask import render_template
from flask import request
from markupsafe import escape
app = Flask(__name__)

def get_routes():
    routes = [str(rule) for rule in app.url_map.iter_rules()]
    routes.pop(0)
    print(routes)
    urls = []
    for route in routes:
        paths = route.split('/')
        path = paths[len(paths) - 1]
        if path != '' and not path.__contains__('<'):
            urls.append(path)
    if len(urls) == 0:
        urls = None
    # print(urls)
    return urls

@app.route('/')
def home():
    urls = get_routes()
    return render_template('index.html', urls=urls)

@app.route('/hostname_form')
def hostname_form():
    urls = get_routes()
    return render_template('hostname_form.html', urls=urls)

@app.route('/hostname', methods=['POST'])
def hostname():
    urls = get_routes()
    hname = request.get_json()['hostname']
    # print(f'hostname: {hname}')
    return render_template('hostname.html', hostname=hname, urls=urls)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    urls = get_routes()
    return render_template('hello.html', name=name, urls=urls)

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'

if __name__ == '__main__':
    app.run(debug=True)