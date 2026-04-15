console.log("✅ content.js loaded");
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {

    let box = document.createElement("div");

    box.style.position = "fixed";
    box.style.top = "20px";
    box.style.right = "20px";
    box.style.padding = "15px";
    box.style.zIndex = "9999";
    box.style.borderRadius = "10px";
    box.style.color = "white";
    box.style.fontSize = "14px";
    box.style.fontWeight = "bold";
    box.style.boxShadow = "0 0 10px rgba(0,0,0,0.5)";

    // 🎨 Color based on result
    if (message.status.includes("Legitimate")) {
        box.style.background = "green";
    } else if (message.status.includes("Suspicious")) {
        box.style.background = "orange";
    } else {
        box.style.background = "red";
    }

    box.innerText = 
`Domain: ${message.domain}
Status: ${message.status}
Score: ${message.score}`;

    document.body.appendChild(box);

    // remove after 5 seconds
    setTimeout(() => box.remove(), 5000);
});
