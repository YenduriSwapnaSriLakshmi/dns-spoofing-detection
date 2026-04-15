chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {

    // Run only when page fully loaded
    if (changeInfo.status !== "complete" || !tab.url) return;

    // Only http/https
    if (!tab.url.startsWith("http")) return;

    try {
        let url= new URL(tab.url);
        let domain = url.hostname;

        // Ignore unwanted domains
        if (
            domain === "127.0.0.1" ||
            domain === "localhost" ||
            domain.includes("chrome") ||
            domain.includes("extensions")
        ) return;

        // Call Flask backend
        fetch("http://127.0.0.1:5000/api/check", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ domain: domain })
        })
        .then(res => res.json())
        .then(data => {

            // Inject popup into page
            chrome.scripting.executeScript({
                target: { tabId: tabId },
                func: (data) => {

                    // Remove old popup if exists
                    let old = document.getElementById("dns-popup");
                    if (old) old.remove();

                    let box = document.createElement("div");
                    box.id = "dns-popup";

                    box.style.position = "fixed";
                    box.style.top = "20px";
                    box.style.right = "20px";
                    box.style.padding = "15px";
                    box.style.zIndex = "9999";
                    box.style.borderRadius = "10px";
                    box.style.color = "white";
                    box.style.fontSize = "13px";
                    box.style.fontWeight = "bold";
                    box.style.whiteSpace = "pre-line";
                    box.style.boxShadow = "0 0 10px rgba(0,0,0,0.5)";

                    // Color based on result
                    if (data.status.includes("Legitimate")) {
                        box.style.background = "green";
                    } else if (data.status.includes("Suspicious")) {
                        box.style.background = "orange";
                    } else {
                        box.style.background = "red";
                    }

                    // Popup content
                    box.innerText =
`🔹 Request
Domain: ${data.request_domain}
IP: ${data.request_ip}
TTL: ${data.request_ttl}

🔹 Response
Domain: ${data.response_domain}
IP: ${data.response_ip}
TTL: ${data.response_ttl}

🔹 Result
Score: ${data.score}
Status: ${data.status}`;

                    document.body.appendChild(box);

                    // Auto remove after 5 sec
                    setTimeout(() => {
                        if (box) box.remove();
                    }, 5000);

                },
                args: [data]
            });

        })
        .catch(err => console.error("API Error:", err));

    } catch (e) {
        console.log("Invalid URL");
    }
});
