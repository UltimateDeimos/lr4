from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int, default=0)
    var_2 = request.form.get("var_2", type=int, default=0)
    operation = request.form.get("operation")
    if operation == 'Addition':
        res = var_1 + var_2
    elif operation == 'Subtraction':
        res = var_1 - var_2
    elif operation == 'Multiplication':
        res = var_1 * var_2
    elif operation == 'Division':
        if var_2 == 0:
            res = 'Division_by_0'
        else:
            res = var_1 / var_2
    else:
        res = 0
    entry = res
    return render_template('form.html', entry=entry)


if __name__ == '__main__':
    app.run(debug=True)