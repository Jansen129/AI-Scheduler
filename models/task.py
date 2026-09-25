from datetime import datetime
from typing import Optional


# Each task has a name, duration(minutes), and default priority(1-5, 1 is highest) of 3
# A task can have an optional deadline, and/or fixed start time
class Task:
    def __init__(
        self,
        name: str,
        duration: int,
        deadline: Optional[datetime] = None,
        priority: int = 3,
        fixed_start: Optional[datetime] = None
    ):
        self.name = name
        self.duration = duration
        self.deadline = deadline
        self.priority = priority
        self.fixed_start = fixed_start 

    def is_fixed(self) -> bool:
        return self.fixed_start is not None

    def has_deadline(self) -> bool:
        return self.deadline is not None

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "duration": self.duration,
            "deadline": self.deadline.isoformat() if self.deadline else None,
            "priority": self.priority,
            "fixed_start": self.fixed_start.isoformat() if self.fixed_start else None
        }

    def __repr__(self):
        return f"Task(name={self.name}, duration={self.duration}, deadline={self.deadline}, priority={self.priority}, fixed_start={self.fixed_start})"