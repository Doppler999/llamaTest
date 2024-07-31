// Updated API URL
import React, { useState } from "react";


const App = () => {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError(null);
    setResult(null);

    try {
      const response = await fetch("https://llamatest.onrender.com/api/v1/sentiment", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await response.json();
      setResult(data.sentiment);
    } catch (error) {
      setError("Failed to analyze sentiment. Please try again.");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
      <div className="max-w-md w-full bg-white shadow-lg rounded-lg p-6 text-center">
        <h1 className="text-2xl font-bold mb-4">Sentiment Analysis Tool</h1>
        <form onSubmit={handleSubmit} className="space-y-4">
          <textarea
            className="w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            rows="5"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Enter your text here..."
            required
          />
          <button
            type="submit"
            className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
          >
            Analyze Sentiment
          </button>
        </form>
        {error && <p className="text-red-500 mt-4">{error}</p>}
        {result && (
          <div className="mt-4">
            <h2 className="text-xl font-semibold">Sentiment Result:</h2>
            <p className="text-lg">{result}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default App;
