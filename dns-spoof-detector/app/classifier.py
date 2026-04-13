def classify(score):
    if score >= 50:
        return "Legitimate ✅"
    else:
        return "Spoofed ❌"