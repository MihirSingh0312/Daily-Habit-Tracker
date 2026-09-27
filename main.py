# main.py
from data_handler import load_data
from habit_manager import add_habit, edit_habit, delete_habit, mark_complete
from reporter import display_habits, show_statistics, export_report

def print_menu():
    print("\n" + "=" * 45)
    print("       DAILY HABIT TRACKER")
    print("=" * 45)
    print("1. Add New Habit")
    print("2. View All Habits")
    print("3. Edit Habit")
    print("4. Delete Habit")
    print("5. Mark Habit Complete (Today)")
    print("6. View Statistics & Streaks")
    print("7. Export Report")
    print("0. Exit")
    print("=" * 45)

def main():
    habits = load_data()
    print("Welcome to Daily Habit Tracker!")

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            display_habits(habits)
        elif choice == "3":
            edit_habit(habits)
        elif choice == "4":
            delete_habit(habits)
        elif choice == "5":
            mark_complete(habits)
        elif choice == "6":
            show_statistics(habits)
        elif choice == "7":
            export_report(habits)
        elif choice == "0":
            print("\nAll data saved. Keep building good habits! Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()