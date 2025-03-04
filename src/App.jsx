import { useState } from "react";
import InputForm from "/src/components/InputForm";
import ResultDisplay from "/src/components/ResultDisplay";
import "./styles.css";

function App() {
  const [result, setResult] = useState(null);
  
  return (
      <div className="form-container">
        <h1>Ski Equipment Recommendation Tool</h1>
        <InputForm setResult={setResult} />
        {result && <ResultDisplay result={result} />}
      </div>
  );
}


export default App;


