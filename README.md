# DNS Spoofing Detection Tool

## 📌 Overview
This project detects DNS spoofing attacks by analyzing DNS responses using:
- IP comparison
- TTL validation
- ASN verification
- Trust scoring

## 🚀 How it works
1. User enters a domain
2. Local DNS response is captured
3. Trusted DNS (Google/Cloudflare) is queried
4. Features are compared
5. Trust score is calculated
6. Output: Legitimate / Suspicious / Spoofed

## ▶️ Run the project
```bash
pip install -r requirements.txt
python run.py