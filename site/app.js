// site/app.js
// Navigation laden, Markdown-Dateien rendern, MathJax triggern

const navList = document.getElementById("nav-list");
const contentEl = document.getElementById("content");

// Hilfsfunktion: Markdown laden und rendern
async function loadMarkdown(path) {
  try {
    const response = await fetch(path);
    if (!response.ok) {
      contentEl.innerHTML = `<h2>Fehler</h2><p>Die Datei <code>${path}</code> konnte nicht geladen werden.</p>`;
      return;
    }
    const text = await response.text();
    const html = marked.parse(text);
    contentEl.innerHTML = html;

    // MathJax neu rendern
    if (window.MathJax && window.MathJax.typesetPromise) {
      window.MathJax.typesetPromise();
    }
  } catch (err) {
    contentEl.innerHTML = `<h2>Fehler</h2><p>Beim Laden von <code>${path}</code> ist ein Fehler aufgetreten.</p>`;
  }
}

// Navigation aus JSON laden
async function loadNavigation() {
  try {
    const response = await fetch("navigation/navigation.json");
    const navData = await response.json();

    navList.innerHTML = "";

    navData.items.forEach((item) => {
      const li = document.createElement("li");
      const btn = document.createElement("button");
      btn.className = "nav-item";
      btn.dataset.path = item.path;

      const icon = document.createElement("img");
      icon.src = item.icon;
      icon.alt = "";

      const span = document.createElement("span");
      span.textContent = item.label;

      btn.appendChild(icon);
      btn.appendChild(span);

      btn.addEventListener("click", () => {
        document
          .querySelectorAll(".nav-item")
          .forEach((el) => el.classList.remove("active"));
        btn.classList.add("active");
        loadMarkdown(item.path);
      });

      li.appendChild(btn);
      navList.appendChild(li);
    });
  } catch (err) {
    navList.innerHTML =
      "<li>Fehler beim Laden der Navigation.</li>";
  }
}

// Initialisierung
document.addEventListener("DOMContentLoaded", () => {
  loadNavigation();
});
