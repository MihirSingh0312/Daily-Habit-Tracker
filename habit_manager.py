# habit_manager.py
from datetime import datetime
from data_handler import get_next_id, save_data, find_habit

def add_habit(habits):
    """Add a new habit."""
    print("\n--- Add New Habit ---")
    name = input("Enter habit name: ").strip()
    if not name:
        print("Habit name cannot be empty.")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    new_habit = {
        "id": get_next_id(habits),
        "name": name,
        "created": today,
        "completions": []
    }
    habits.append(new_habit)
    save_data(habits)
    print(f"Habit '{name}' added successfully! (ID: {new_habit['id']})")

def edit_habit(habits):
    """Edit an existing habit name."""
    from reporter import display_habits
    display_habits(habits)

    if not habits:
        return

    try:
        hid = int(input("\nEnter Habit ID to edit: ").strip())
    except ValueError:
        print("Invalid ID.")
        return

    habit = find_habit(habits, hid)
    if not habit:
        print("Habit not found.")
        return

    new_name = input(f"New name [{habit['name']}]: ").strip()
    if new_name:
        habit["name"] = new_name
        save_data(habits)
        print("Habit updated successfully!")
    else:
        print("No changes made.")

def delete_habit(habits):
    """Delete a habit."""
    from reporter import display_habits
    display_habits(habits)

    if not habits:
        return

    try:
        hid = int(input("\nEnter Habit ID to delete: ").strip())
    except ValueError:
        print("Invalid ID.")
        return

    habit = find_habit(habits, hid)
    if not habit:
        print("Habit not found.")
        return

    confirm = input(f"Delete '{habit['name']}'? (y/n): ").strip().lower()
    if confirm == "y":
        habits.remove(habit)
        save_data(habits)
        print("Habit deleted.")
    else:
        print("Cancelled.")

def mark_complete(habits):
    """Mark a habit as completed for today."""
    from reporter import display_habits
    display_habits(habits)

    if not habits:
        return

    try:
        hid = int(input("\nEnter Habit ID to mark complete: ").strip())
    except ValueError:
        print("Invalid ID.")
        return

    habit = find_habit(habits, hid)
    if not habit:
        print("Habit not found.")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    if today in habit["completions"]:
        print(f"'{habit['name']}' is already marked complete for today.")
        return

    habit["completions"].append(today)
    habit["completions"].sort()
    save_data(habits)
    print(f"'{habit['name']}' marked as complete for {today}!")