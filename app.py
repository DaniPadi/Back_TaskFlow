from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_restx import Api

from modules.tasks.routes.task_routes import task_ns
from config.routes.db_routes import health_ns


app = Flask(__name__)
api = Api(app, doc="/docs")

api.add_namespace(task_ns)
api.add_namespace(health_ns)

if __name__ == "__main__":
    app.run(debug=True)