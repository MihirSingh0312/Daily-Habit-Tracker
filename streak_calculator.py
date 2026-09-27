# streak_calculator.py
from datetime import datetime, timedelta

def calculate_current_streak(completions):
    """Calculate current consecutive streak ending today."""
    if not completions:
        return 0

    completions = sorted(completions, reverse=True)
    today = datetime.now().date()
    streak = 0
    expected = today

    for date_str in completions:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        if date == expected:
            streak += 1
            expected -= timedelta(days=1)
        elif date < expected:
            break
    return streak

def calculate_longest_streak(completions):
    """Calculate the longest streak ever achieved."""
    if not completions:
        return 0

    dates = sorted([datetime.strptime(d, "%Y-%m-%d").date() for d in completions])
    longest = current = 1

    for i in range(1, len(dates)):
        if dates[i] == dates[i-1] + timedelta(days=1):
            current += 1
            longest = max(longest, current)
        else:
            current = 1
    return longest