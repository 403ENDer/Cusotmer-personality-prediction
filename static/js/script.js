document.addEventListener("DOMContentLoaded", function () {
  const resultContent = document.getElementById("result-content");

  // Simulate typing effect
  resultContent.textContent = "";
  let index = 0;

  function typeText() {
    if (index < predictionResult.length) {
      resultContent.textContent += predictionResult.charAt(index);
      index++;
      setTimeout(typeText, 50); // Adjust the typing speed here
    } else {
      resultContent.classList.add("typing-complete");
    }
  }

  typeText();
});
