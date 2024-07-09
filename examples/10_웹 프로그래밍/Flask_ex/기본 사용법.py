from flask import Flask, render_template, request

app = Flask(__name__)


# 라우팅 설정
@app.route('/')
def index():
    return "Hello, World!"


@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            <input type="submit" value="Submit">
        </form>
    '''


if __name__ == '__main__':
    app.run(debug=True)
