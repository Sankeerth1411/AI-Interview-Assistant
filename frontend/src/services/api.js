const BASE_URL = "http://127.0.0.1:8000";

export async function getQuestion(role, difficulty) {
  const response = await fetch(`${BASE_URL}/question`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      role,
      difficulty,
    }),
  });

  return await response.json();
}

export async function evaluateAnswer(question, answer) {
  const response = await fetch(`${BASE_URL}/evaluate`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      question,
      answer,
    }),
  });

  return await response.json();
}