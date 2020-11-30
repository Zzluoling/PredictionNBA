from flask import Flask
import route
import service

app = Flask(__name__)
app.config['SECRET_KEY'] = "flask"
service.init_app(app)
route.init_app(app)


if __name__ == '__main__':
    app.run()
