from flask import Flask, render_template, request, jsonify

from app.dns_resolver import get_local_dns, get_trusted_dns
from app.asn_lookup import get_asn
from app.trust_score import calculate_trust
from app.classifier import classify
from app.config import DNS_SERVERS
from app.simulator import is_attack_active

app = Flask(__name__)

stats = {
    "total": 0,
    "legit": 0,
    "spoofed": 0,
    "history": []
}

ATTACK_SITES = ["google.com", "yahoo.com", "instagram.com", "facebook.com", "twitter.com"]

def is_target(domain):
    domain = domain.lower().replace("www.", "")
    return domain in ATTACK_SITES or any(domain.endswith("." + site) for site in ATTACK_SITES)


@app.route("/api/check", methods=["POST"])
def api_check():
    data = request.get_json()
    domain = data.get("domain")

    local_ip, local_ttl = get_local_dns(domain)

    trusted_ip, trusted_ttl = None, None
    for server in DNS_SERVERS:
        trusted_ip, trusted_ttl = get_trusted_dns(domain, server)
        if trusted_ip:
            break

    # 🚨 SIMULATION
    if is_attack_active() and is_target(domain):
        trusted_ip = "1.2.3.4"

    asn = get_asn(local_ip) if local_ip else None

    score = calculate_trust(domain, local_ip, trusted_ip, local_ttl, trusted_ttl, asn)
    status = classify(score)

    # ✅ FIX FOR MOBILE NETWORK (IMPORTANT)
    if not local_ip:
        local_ip = "Not Available"
    if not local_ttl:
        local_ttl = "Not Available"
    if not trusted_ip:
        trusted_ip = "Not Available"
    if not trusted_ttl:
        trusted_ttl = "Not Available"

    # 📊 Stats update
    stats["total"] += 1
    if "Legitimate" in status:
        stats["legit"] += 1
    else:
        stats["spoofed"] += 1

    stats["history"].append({
        "domain": domain,
        "status": status,
        "score": score
    })
    stats["history"] = stats["history"][-5:]

    return jsonify({
        "request_domain": domain,
        "request_ip": local_ip,
        "request_ttl": local_ttl,

        "response_domain": domain,
        "response_ip": trusted_ip,
        "response_ttl": trusted_ttl,

        "score": score,
        "status": status
    })


@app.route("/")
def dashboard():
    return render_template("dashboard.html", stats=stats)


@app.route("/stats")
def get_stats():
    return jsonify(stats)


if __name__ == "__main__":
    app.run(debug=True)