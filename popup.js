document.getElementById("checkButton").addEventListener("click", async () => {

    const emailText = document.getElementById("emailContent").value;
    const resultElement = document.getElementById("result");


    if (!emailText.trim()) {
        resultElement.innerHTML = `<strong>Please enter email content!</strong>`;
        resultElement.className = "";
        return;
    }



    try {
        const response = await fetch("http://127.0.0.1:5000/detect", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email_text: emailText }),
        });



        const data = await response.json();

        if (response.ok) {
            resultElement.innerHTML = `<strong>${data.result}</strong><br><span>Confidence: ${(data.confidence * 100).toFixed(2)}%</span>`;
            resultElement.className = data.result === "Phishing" ? "phishing" : "not-phishing";

        } else {
            resultElement.innerHTML = `<strong>${data.error || "Error detecting phishing!"}</strong>`;
            resultElement.className = "";

        }
    } catch (error) {
        resultElement.innerHTML = `<strong>Error connecting to server!</strong>`;

        resultElement.className = "";

        
    }
});
