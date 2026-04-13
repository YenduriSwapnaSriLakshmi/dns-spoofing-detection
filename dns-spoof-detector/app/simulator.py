# app/simulator.py

import os

# ✅ Absolute path (fixes your issue)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLAG_FILE = os.path.join(BASE_DIR, "attack_mode.txt")


def enable_attack():
    with open(FLAG_FILE, "w") as f:
        f.write("ON")


def disable_attack():
    if os.path.exists(FLAG_FILE):
        os.remove(FLAG_FILE)


def is_attack_active():
    return os.path.exists(FLAG_FILE)