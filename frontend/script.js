document.getElementById("salaryForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const age = parseFloat(document.getElementById("age").value);
  const pts = parseFloat(document.getElementById("pts").value);
  const gp = parseFloat(document.getElementById("gp").value);
  const ft = parseFloat(document.getElementById("ft").value);

  const payload = {
    Age: age,
    PTS: pts,
    GP: gp,
    "FT%": ft,
  };

  const resultDiv = document.getElementById("result");
  resultDiv.textContent = "Predicting...";

  try {
    const response = await fetch("https://nba-salary-predictor.onrender.com/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    const data = await response.json();
    if (response.ok) {
      resultDiv.textContent = `Predicted Salary: $${data.predicted_salary.toLocaleString()}`;
    } else {
      resultDiv.textContent = `Error: ${data.error}`;
    }
  } catch (err) {
    resultDiv.textContent = `Error: ${err.message}`;
  }
});
