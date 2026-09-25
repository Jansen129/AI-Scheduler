from datetime import datetime, timedelta
from .task import Task

# TimeBlock will only be created if there is a task to go there
# Each TimeBlock has a start time, end time, and a task assigned to it.
# The end time is calculated based on the start time and the task's duration.
class TimeBlock:
    def __init__(
        self,
        start_time: datetime,
        task: Task
    ):
        self.start_time = start_time
        self.task = task
        self.end_time = start_time + timedelta(minutes=self.task.duration)

    def to_dict(self) -> dict:
        return {
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "task": self.task.to_dict()
        }

    def __repr__(self):
        return f"TimeBlock(start_time={self.start_time}, end_time={self.end_time}, task={self.task.name})"