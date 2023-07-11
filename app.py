from flask import Flask
from views.customer_blueprint import customer_bp

app = Flask(__name__)
app.register_blueprint(customer_bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
