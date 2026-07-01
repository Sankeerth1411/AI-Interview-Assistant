import os
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


def generate_interview_question(role, difficulty):
    try:
        prompt = f"""
        Generate ONE interview question.

        Role: {role}
        Difficulty: {difficulty}

        Rules:
        - Ask only one question.
        - Do not provide the answer.
        - Keep it relevant to the role.
        - Return only the question text.
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        question = response.text.strip()
        print(f"\n--- {difficulty} {role} Interview Question ---")
        print(question)
        print("------------------------------------------------\n")
        return question

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def evaluate_answer(question, user_answer):
    try:

        prompt = f"""
You are a professional technical interviewer.

Question:
{question}

Candidate Answer:
{user_answer}

Scoring Rubric:
0-2 = Incorrect or irrelevant
3-4 = Very limited understanding
5-6 = Basic understanding
7-8 = Good understanding with relevant explanation
9-10 = Excellent and complete answer

Return ONLY in this format:

Score: X/10

Strength: <one short sentence>

Weakness: <one short sentence>

Improvement: <one short sentence>

Rules:
- Maximum 10 words per point.
- No bullet points.
- No markdown.
- No explanations.
- No extra text.
- Be strict with scoring.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("\n===== EVALUATION =====")
        print(response.text)

    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":

    roles = {
        1: "Data Analyst",
        2: "Data Scientist",
        3: "Machine Learning Engineer",
        4: "AI Engineer",
        5: "Data Engineer",
        6: "MLOps Engineer",
        7: "NLP Engineer",
        8: "Computer Vision Engineer",
        9: "Software Engineer",
        10: "Business Analyst",
        11: "Mixed Interview"
    }

    difficulties = {
        1: "Beginner",
        2: "Intermediate",
        3: "Advanced"
    }

    print("\n========== INTERVIEW ROLE SELECTION ==========\n")

    for key, value in roles.items():
        print(f"{key}. {value}")

    role_choice = int(input("\nSelect a role (1-11): "))

    if role_choice not in roles:
        print("Invalid role selected.")
        exit()

    role = roles[role_choice]

    print("\n========== DIFFICULTY LEVEL ==========\n")

    for key, value in difficulties.items():
        print(f"{key}. {value}")

    difficulty_choice = int(input("\nSelect difficulty (1-3): "))

    if difficulty_choice not in difficulties:
        print("Invalid difficulty selected.")
        exit()

    difficulty = difficulties[difficulty_choice]

    if role == "Mixed Interview":
        role = """
        Mix questions from:
        - Data Analyst
        - Data Scientist
        - Machine Learning Engineer
        - AI Engineer
        - Data Engineer
        - MLOps Engineer
        - NLP Engineer
        - Computer Vision Engineer
        - Software Engineer
        - Business Analyst
        """
    question = generate_interview_question(role, difficulty)

    if question is not None:

        answer = input("\nYour Answer:\n")

        evaluate_answer(question, answer)