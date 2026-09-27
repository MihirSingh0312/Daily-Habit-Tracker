# reporter.py
from datetime import datetime
from streak_calculator import calculate_current_streak, calculate_longest_streak

def display_habits(habits):
    """Display all habits in a table format."""
    if not habits:
        print("\nNo habits found.")
        return

    print("\n" + "=" * 60)
    print(f"{'ID':<5} {'Habit Name':<25} {'Created':<12} {'Completions'}")
    print("=" * 60)
    for h in habits:
        print(f"{h['id']:<5} {h['name']:<25} {h['created']:<12} {len(h['completions'])}")
    print("=" * 60)

def show_statistics(habits):
    """Show detailed statistics for all habits."""
    print("\n" + "=" * 50)
    print("           HABIT STATISTICS")
    print("=" * 50)

    if not habits:
        print("No habits available.")
        return

    for h in habits:
        created_date = datetime.strptime(h["created"], "%Y-%m-%d").date()
        total_days = (datetime.now().date() - created_date).days + 1
        completed = len(h["completions"])
        rate = (completed / total_days * 100) if total_days > 0 else 0
        current = calculate_current_streak(h["completions"])
        longest = calculate_longest_streak(h["completions"])

        print(f"\nHabit: {h['name']}")
        print(f"  Completions     : {completed}")
        print(f"  Current Streak  : {current} day(s)")
        print(f"  Longest Streak  : {longest} day(s)")
        print(f"  Completion Rate : {rate:.1f}%")

    print("=" * 50)

def export_report(habits):
    """Export a text report."""
    filename = "habit_report.txt"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("=" * 50 + "\n")
            f.write("         DAILY HABIT TRACKER REPORT\n")
            f.write("=" * 50 + "\n\n")

            if not habits:
                f.write("No habits recorded.\n")
            else:
                for h in habits:
                    current = calculate_current_streak(h["completions"])
                    longest = calculate_longest_streak(h["completions"])
                    f.write(f"Habit: {h['name']}\n")
                    f.write(f"  Created           : {h['created']}\n")
                    f.write(f"  Total Completions : {len(h['completions'])}\n")
                    f.write(f"  Current Streak    : {current}\n")
                    f.write(f"  Longest Streak    : {longest}\n\n")

            f.write("=" * 50 + "\n")
        print(f"\nReport exported to '{filename}'")
    except IOError:
        print("Error writing report file.")