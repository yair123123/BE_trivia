from dataclasses import dataclass


@dataclass
class Answer:
    question_id: int
    text_answer: str
    correct: bool
    answer_id: int = None