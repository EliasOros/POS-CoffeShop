from flask import Flask
from config import Config
from model import db
from users.routes import usuarios_bp


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(usuarios_bp)

if __name__ == '__main__':
    app.run(debug=True)
