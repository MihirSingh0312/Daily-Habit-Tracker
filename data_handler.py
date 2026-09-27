# data_handler.py
import json
import os
from config import DATA_FILE

def load_data():
    """Load habits from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        print("Warning: Could not read data file. Starting fresh.")
        return []

def save_data(habits):
    """Save habits to JSON file."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(habits, f, indent=4)
        return True
    except IOError:
        print("Error: Could not save data.")
        return False

def get_next_id(habits):
    """Generate next unique ID."""
    if not habits:
        return 1
    return max(h["id"] for h in habits) + 1

def find_habit(habits, habit_id):
    """Find a habit by ID."""
    for h in habits:
        if h["id"] == habit_id:
            return h
    return None