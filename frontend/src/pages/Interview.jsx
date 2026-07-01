import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { getQuestion, evaluateAnswer } from "../services/api";
import "../styles/interview.css";

function Interview() {
  const location = useLocation();
  const navigate = useNavigate();

  const state = location.state;

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadQuestion() {
      try {
        if (!state) {
          alert("No interview details received.");
          navigate("/");
          return;
        }

        const { role, difficulty } = state;

        const data = await getQuestion(role, difficulty);

        setQuestion(data.question);
      } catch (error) {
        console.error(error);
        alert("Failed to generate interview question.");
      } finally {
        setLoading(false);
      }
    }

    loadQuestion();
  }, [state, navigate]);

  async function submitAnswer() {
    if (answer.trim() === "") {
      alert("Please enter your answer.");
      return;
    }

    try {
      const result = await evaluateAnswer(question, answer);

      navigate("/result", {
        state: result,
      });
    } catch (error) {
      console.error(error);
      alert("Failed to evaluate answer.");
    }
  }

  if (loading) {
    return (
      <div className="loading-container">
        <div className="loader"></div>
        <h2>Generating Interview Question...</h2>
      </div>
    );
  }

  return (
    <div className="interview-container">

      <h1>AI Interview Assistant</h1>

      <div className="details">

        <div>
          <strong>Role</strong>
          <span>{state.role}</span>
        </div>

        <div>
          <strong>Difficulty</strong>
          <span>{state.difficulty}</span>
        </div>

        <div>
          <strong>Questions</strong>
          <span>{state.questionCount}</span>
        </div>

      </div>

      <div className="question-card">

        <h2>Interview Question</h2>

        <p>{question}</p>

      </div>

      <div className="answer-section">

        <label>Your Answer</label>

        <textarea
          rows="10"
          value={answer}
          onChange={(e) => setAnswer(e.target.value)}
          placeholder="Type your answer here..."
        />

        <div className="char-count">

          {answer.length} characters

        </div>

      </div>

      <button
        className="submit-btn"
        onClick={submitAnswer}
      >
        Submit Answer
      </button>

    </div>
  );
}

export default Interview;