from flask import Flask
from flask_restx import Api
from modules.tasks.routes.task_routes import task_ns

app = Flask(__name__)
api = Api(app, doc="/docs")

api.add_namespace(task_ns)

if __name__ == "__main__":
    app.run(debug=True)