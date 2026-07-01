from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel
from service.gemini import generate_interview_question, evaluate_answer
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    role: Literal[
        "Software Engineer",
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist",
        "Data Analyst",
        "Frontend Developer",
        "Backend Developer",
        "Full Stack Developer",
        "Python Developer",
        "Java Developer",
        "DevOps Engineer",
        "Cloud Engineer"
    ]
    difficulty: Literal[
        "Beginner",
        "Intermediate",
        "Advanced"
    ]

class AnswerRequest(BaseModel):
    question: str
    answer: str


@app.get("/")
def home():
    return {"message": "Interview API Running"}

@app.get("/roles")
def get_roles():
    return {
        "roles": [
            "Software Engineer",
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Scientist",
            "Data Analyst",
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Developer",
            "Python Developer",
            "Java Developer",
            "DevOps Engineer",
            "Cloud Engineer"
        ]
    }


@app.get("/difficulties")
def get_difficulties():
    return {
        "difficulties": [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    }


@app.post("/question")
def question(data: QuestionRequest):
    try:
        q = generate_interview_question(
            data.role,
            data.difficulty
        )

        return {"question": q}

    except Exception as e:
        return {"error": str(e)}


@app.post("/evaluate")
def evaluate(data: AnswerRequest):
    try:
        result = evaluate_answer(
            question=data.question,
            answer=data.answer
        )

        return result

    except Exception as e:
        return {"error": str(e)}