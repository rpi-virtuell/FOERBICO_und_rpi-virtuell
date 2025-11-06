<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Must-have / Not-have – Digitale Fortbildungen</title>
<style>
  body {
    font-family: system-ui, sans-serif;
    background: #f7f7f9;
    padding: 2rem;
    color: #222;
  }
  h1 { text-align: center; margin-bottom: 2rem; }
  .item {
    margin-bottom: 2rem;
    background: white;
    padding: 1rem 1.5rem;
    border-radius: 1rem;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  }
  label {
    display: block;
    font-weight: 600;
    margin-bottom: .5rem;
  }
  input[type=range] {
    width: 100%;
  }
  .value {
    text-align: right;
    font-size: 0.9rem;
    color: #555;
  }
</style>
</head>
<body>

<h1>Must-have / Not-have<br>für digitale Fortbildungen</h1>

<div id="sliderContainer"></div>

<script>
const items = [
  "Flexible Zeiteinteilung",
  "Praxisnahe Inhalte",
  "Einfacher technischer Zugang",
  "Austausch & Community",
  "Interaktive Methoden",
  "Asynchrone Lernmöglichkeiten",
  "Offene Materialien (OER)",
  "Verbindlichkeit & Motivation"
];

const container = document.getElementById("sliderContainer");

items.forEach((text, i) => {
  const div = document.createElement("div");
  div.className = "item";
  div.innerHTML = `
    <label>${text}</label>
    <input type="range" min="0" max="10" value="5" id="slider${i}">
    <div class="value">Neutral</div>
  `;
  container.appendChild(div);
  
  const slider = div.querySelector("input");
  const valueLabel = div.querySelector(".value");
  slider.addEventListener("input", () => {
    const val = slider.value;
    if (val < 4) valueLabel.textContent = "Not have";
    else if (val < 7) valueLabel.textContent = "Neutral";
    else valueLabel.textContent = "Must have";
  });
});
</script>

</body>
</html>