from enum import Enum

class TaskType(Enum):
    Bug = "BUG"
    Feature = "FEATURE"
    Task = "TASK"
    Improvement = "IMPROVEMENT"


class PriorityTask(Enum):
    Low = "BAJA"
    Medium = "MEDIA"
    High = "ALTA"
    Urgent = "URGENTE"


class TaskStatus(Enum):
    To_Do = "Por hacer"
    In_Progress = "En progreso"
    On_Review = "En revisión"
    Done = "Completado"
