from app.trust_score import calculate_trust

def test_score():
    score = calculate_trust("1.1.1.1", "1.1.1.1", 100, 100, "13335")
    assert score > 0