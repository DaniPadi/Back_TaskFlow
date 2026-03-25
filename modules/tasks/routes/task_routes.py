from flask_restx import Namespace, Resource, fields
from modules.tasks.builder.task_builder import TaskBuilder
from modules.tasks.models.enum import TaskType, TaskStatus, PriorityTask


task_ns = Namespace("tasks", description="Task operations")

# Modelo para documentación (Swagger)
task_model = task_ns.model("Task", {
    "type": fields.String(required=True, description="Task type", example= "BUG"),
    "title": fields.String(required=True, example= "Error en Login"),
    "description": fields.String(required=True, example= "No deja iniciar sesión"),
    "status": fields.String(required=True, example= "Por hacer"),
    "priority": fields.String(required=True, example= "ALTA"),
    "extra": fields.Raw(required=False)
})


# "Base de datos" temporal
tasks = []


@task_ns.route("/")
class TaskList(Resource):

    @task_ns.marshal_list_with(task_model)
    def get(self):
        return [task.to_dict() for task in tasks]


    @task_ns.expect(task_model)
    def post(self):
        data = task_ns.payload

        try:
            builder = TaskBuilder()

            task = (
                builder
                .set_type(TaskType(data["type"]))
                .set_title(data["title"])
                .set_description(data["description"])
            )

            # opcionales
            if "status" in data:
                task.set_status(TaskStatus(data["status"]))

            if "priority" in data:
                task.set_priority(PriorityTask(data["priority"]))

            if "extra" in data:
                for key, value in data["extra"].items():
                    task.add_extra(key, value)

            task = task.build()

            tasks.append(task)

            return task.to_dict(), 201

        except Exception as e:
            return {"error": str(e)}, 400