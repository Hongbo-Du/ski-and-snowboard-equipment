const ResultDisplay = ({ result }) => {
    if (!result || Object.keys(result).length === 0) {
      return null;
    }

    const recommendation = result["recommendation received"] || {};

  return (
      <div>
        <h2>Your Personalized Ski Recommendations </h2>
        <p><strong>Ski Type:</strong> {recommendation.ski_type || "N/A"}</p>
        <p><strong>Ski Size:</strong> {recommendation.ski_size || "N/A"}</p>
        <p><strong>DIN Setting:</strong> {recommendation.DIN || "N/A"}</p>
        <p><strong>Boot Size:</strong> {recommendation.boot_size || "N/A"}</p>
        <p><strong>Boot Flex:</strong> {recommendation.boot_flex || "N/A"}</p>
      </div>
    );
  };
  
  export default ResultDisplay;
  