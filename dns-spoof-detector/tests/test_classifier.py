from app.classifier import classify

def test_classifier():
    assert classify(80) == "Legitimate ✅"
    assert classify(50) == "Suspicious ⚠"
    assert classify(10) == "Spoofed ❌"