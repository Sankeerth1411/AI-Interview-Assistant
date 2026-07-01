import { useLocation, useNavigate } from "react-router-dom";
import "../styles/result.css";

function Result() {
  const { state } = useLocation();
  const navigate = useNavigate();

  if (!state) {
    return (
      <div className="result-container">
        <h1>No Result Found</h1>

        <button
          className="result-btn"
          onClick={() => navigate("/")}
        >
          Back to Home
        </button>
      </div>
    );
  }

  return (
    <div className="result-container">

      <h1>Interview Result</h1>

      <div className="score-card">

        <h2>Your Score</h2>

        <div className="score">
          {state.score}
        </div>

      </div>

      <div className="feedback-card">

        <h3>Strength</h3>

        <p>{state.strength}</p>

      </div>

      <div className="feedback-card">

        <h3>Weakness</h3>

        <p>{state.weakness}</p>

      </div>

      <div className="feedback-card">

        <h3>AI Feedback</h3>

        <p>{state.feedback}</p>

      </div>

      <button
        className="result-btn"
        onClick={() => navigate("/")}
      >
        Take Another Interview
      </button>

    </div>
  );
}

export default Result;