from flask import request
from flask_restx import Namespace, Resource, fields

from modules.tasks.services.tasks_service import TaskService
from modules.tasks.repository.task_repository import TaskRepository

task_ns = Namespace('tasks', description='Task operations')
repository = TaskRepository()
service = TaskService(repository)

task_model = task_ns.model('Task', {
    'title': fields.String(required=True, example="Implement login feature"),
    'description': fields.String(example="Create authentication using JWT"),
    'due_date': fields.String(required=True, example="2026-03-30T12:00:00"),
    'priority': fields.String(example="ALTA"),
    'type': fields.String(example="FEATURE")
})

move_model = task_ns.model('MoveTask', {'column_id': fields.Integer(required=True, example=2)})
comment_model = task_ns.model('Comment', {'comment': fields.String(required=True, example="Needs review")})
time_model = task_ns.model('TimeLog', {'hours': fields.Float(required=True, example=3.5)})
attachment_model = task_ns.model('Attachment', {'file': fields.String(required=True, example="design.png")})

# CRUD
@task_ns.route('/')
class TaskList(Resource):
    def get(self):
        return service.get_all_tasks(), 200

    @task_ns.expect(task_model)
    def post(self):
        data = request.json
        return service.create_task(data), 201

@task_ns.route('/<int:id>')
class Task(Resource):
    def get(self, id):
        task = service.get_task(id)
        if not task:
            return {"error": "Not found"}, 404
        return task.to_dict()

    @task_ns.expect(task_model)
    def put(self, id):
        data = request.json
        task = service.update_task(id, data)
        if not task:
            return {"error": "Not found"}, 404
        return task.to_dict()

    def delete(self, id):
        task = service.delete_task(id)
        if not task:
            return {"error": "Not found"}, 404
        
        return {"message": "Deleted"}, 200

# Move Task
@task_ns.route('/<int:id>/move')
class MoveTask(Resource):
    @task_ns.expect(move_model)
    def post(self, id):
        data = request.json
        task = service.move_task(id, data["column_id"])
        if not task:
            return {"error": "Not found"}, 404
        return task

# Add Comment
@task_ns.route('/<int:id>/comment')
class CommentTask(Resource):
    @task_ns.expect(comment_model)
    def post(self, id):
        data = request.json
        task = service.add_comment(id, data["comment"])
        if not task:
            return {"error": "Not found"}, 404
        return task

# Add Time Log
@task_ns.route('/<int:id>/timelog')
class TimeLogTask(Resource):
    @task_ns.expect(time_model)
    def post(self, id):
        data = request.json
        task = service.add_time_log(id, data["hours"])
        if not task:
            return {"error": "Not found"}, 404
        return task

# Add Attachment
@task_ns.route('/<int:id>/attachment')
class AttachmentTask(Resource):
    @task_ns.expect(attachment_model)
    def post(self, id):
        data = request.json
        task = service.add_attachment(id, data["file"])
        if not task:
            return {"error": "Not found"}, 404
        
        return task.to_dict()

# Clone Task
@task_ns.route('/<int:id>/clone')
class CloneTask(Resource):
    def post(self, id):
        task = service.clone_task(id)
        if not task:
            return {"error": "Not found"}, 404
        return task

# Deadline Hours
@task_ns.route('/<int:id>/deadline')
class DeadlineTask(Resource):
    def get(self, id):
        hours = service.get_deadline_hours(id)
        if hours is None:
            return {"error": "Not found"}, 404
        return {"hours_remaining": hours}