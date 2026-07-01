import os
import time
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Please check your .env file.")

# Initialize Gemini Client
client = genai.Client(api_key=api_key)


def call_gemini_with_retry(prompt, retries=3, wait=10):
    """Call Gemini API with automatic retry on 503 errors."""
    for attempt in range(1, retries + 1):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response
        except Exception as e:
            error_msg = str(e)
            if "503" in error_msg or "UNAVAILABLE" in error_msg:
                if attempt < retries:
                    time.sleep(wait)
                else:
                    raise RuntimeError(f"Gemini unavailable after {retries} attempts. Try again later.")
            else:
                raise RuntimeError(f"Gemini API error: {e}")


def generate_interview_question(role: str, difficulty: str) -> str:
    """Generate a single interview question for the given role and difficulty."""
    prompt = f"""
    Generate ONE interview question.

    Role: {role}
    Difficulty: {difficulty}

    Rules:
    - Ask only one question.
    - Do not provide the answer.
    - Keep it relevant to the role.
    - Return only the question text, nothing else.
    """

    response = call_gemini_with_retry(prompt)
    return response.text.strip()


def evaluate_answer(question: str, answer: str) -> dict:
    """Evaluate a single answer and return score + feedback as a dict."""
    prompt = f"""
You are a professional technical interviewer.

Evaluate the candidate's answer to the following question.

Question: {question}
Candidate's Answer: {answer}

Scoring Rubric:
0-2 = Incorrect or irrelevant
3-4 = Very limited understanding
5-6 = Basic understanding
7-8 = Good understanding with relevant explanation
9-10 = Excellent and complete answer

Return ONLY in this exact format (no extra text, no markdown):

Score: X/10
Strength: <one short sentence under 10 words>
Weakness: <one short sentence under 10 words>
Feedback: <one short sentence under 15 words>
"""

    response = call_gemini_with_retry(prompt)
    raw = response.text.strip()

    result = {}
    for line in raw.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            result[key.strip().lower()] = value.strip()

    return {
        "score": result.get("score", "N/A"),
        "strength": result.get("strength", "N/A"),
        "weakness": result.get("weakness", "N/A"),
        "feedback": result.get("feedback", "N/A"),
    }