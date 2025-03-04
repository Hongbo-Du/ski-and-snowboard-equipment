// InputForm.jsx

import { useState } from "react";
import axios from "axios";
import AlertMessage from "./AlertMessage";

const InputForm = ({ setResult }) => {
  const [formData, setFormData] = useState({ height: "", weight: "", level: "", location: "" });
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    
    if (!formData.height || !formData.weight || !formData.location) {
      setError("All fields are required.");
      return;
    }
    
    try {
      const response = await axios.post("http://localhost:8000/recommend", formData, {
        headers: { "Content-Type": "application/json" }
      });
      setResult(response.data);
    } catch (error) {
      setError("Error fetching recommendations.");
    }

  };

  return (
    <div>
      {error && <AlertMessage message={error} />}
      <form onSubmit={handleSubmit}>
        <input type="number" name="height" placeholder="Height (cm)" value={formData.height} onChange={handleChange} />
        <input type="number" name="weight" placeholder="Weight (kg)" value={formData.weight} onChange={handleChange} />
        <input type="text" name="location" placeholder="Ski Location" value={formData.location} onChange={handleChange} />
        <select name="level" value={formData.level} onChange={handleChange} aria-label="Select your ski level">
          <option value="" disabled hidden>Select Your Ski Level</option>
          <option value="beginner">Beginner</option>
          <option value="intermediate">Intermediate</option>
          <option value="expert">Expert</option>
        </select>
        <button type="submit">Get Recommendation</button>
      </form>
    </div>
  );
};

export default InputForm;







