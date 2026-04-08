from typing import Literal, List
from pydantic import BaseModel


class EmailItem(BaseModel):
    email_id: str
    sender: str
    subject: str
    body: str


class Observation(BaseModel):
    task_name: str
    current_email: EmailItem
    step_count: int
    max_steps: int
    completed: List[str]


class Action(BaseModel):
    email_id: str
    classification: Literal["billing", "technical", "meeting", "spam"]
    priority: Literal["low", "medium", "high"]
    decision: Literal["archive", "reply", "escalate", "schedule"]


class Reward(BaseModel):
    score: float
    reason: str


class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: dict