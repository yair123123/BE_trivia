from dataclasses import dataclass

@dataclass
class Question:
    text_question: str
    type : str
    difficulty : str
    category : str
    id : int = None
