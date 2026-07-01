import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/home.css";

function Home() {
  const navigate = useNavigate();

   const roles = [
  {
    title: "AI Engineer",
    desc: "LLMs, NLP, Computer Vision"
  },
  {
    title: "Machine Learning Engineer",
    desc: "Machine Learning & MLOps"
  },
  {
    title: "Data Scientist",
    desc: "Data Analysis & AI Models"
  },
  {
    title: "Data Analyst",
    desc: "SQL, Excel & Visualization"
  },
  {
    title: "Software Engineer",
    desc: "DSA, OOP & System Design"
  },
  {
    title: "Frontend Developer",
    desc: "React, HTML, CSS"
  },
  {
    title: "Backend Developer",
    desc: "APIs, Databases & Servers"
  },
  {
    title: "Full Stack Developer",
    desc: "Frontend + Backend"
  },
  {
    title: "Python Developer",
    desc: "Python Development"
  },
  {
    title: "Java Developer",
    desc: "Java & Spring Boot"
  },
  {
    title: "DevOps Engineer",
    desc: "CI/CD & Docker"
  },
  {
    title: "Cloud Engineer",
    desc: "AWS, Azure & GCP"
  }
];

  const difficulties = [
    "Beginner",
    "Intermediate",
    "Advanced"
  ];

  const [role, setRole] = useState("");
  const [difficulty, setDifficulty] = useState("");
  const [questionCount, setQuestionCount] = useState(10);

  const startInterview = () => {
    if (!role || !difficulty) {
      alert("Please select Role and Difficulty");
      return;
    }

    navigate("/interview", {
      state: {
        role,
        difficulty,
        questionCount,
      },
    });
  };

  return (
    <div className="home-container">

      <h1 className="home-title">
        AI Interview Assistant
      </h1>

      <p className="home-subtitle">
        Practice AI-powered mock interviews for your dream job.
      </p>

      {/* Role */}

      <div className="section">

        <h2>Select Role</h2>

        <div className="role-grid">

          {roles.map((item) => (

            <div
              key={item.title}
              className={`role-card ${
                role === item.title ? "active" : ""
              }`}
              onClick={() => setRole(item.title)}
            >

              <h3>{item.title}</h3>

              <p>{item.desc}</p>

            </div>

          ))}

        </div>

      </div>

      {/* Difficulty */}

      <div className="section">

        <h2>Select Difficulty</h2>

        <div className="difficulty-container">

          {difficulties.map((level) => (

            <div
              key={level}
              className={`difficulty-card ${
                difficulty === level ? "active" : ""
              }`}
              onClick={() => setDifficulty(level)}
            >

              <h3>{level}</h3>

            </div>

          ))}

        </div>

      </div>

      {/* Question Count */}

      <div className="section">

        <h2>Number of Questions</h2>

        <div className="question-box">

          <select
            value={questionCount}
            onChange={(e) =>
              setQuestionCount(Number(e.target.value))
            }
          >
            <option value={5}>5</option>
            <option value={10}>10</option>
            <option value={15}>15</option>
            <option value={20}>20</option>
          </select>

        </div>

      </div>

      <button
        className="start-btn"
        onClick={startInterview}
      >
        Start Interview
      </button>

    </div>
  );
}

export default Home;