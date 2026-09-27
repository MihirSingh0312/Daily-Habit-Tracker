# Daily-Habit-Tracker
A lightweight, terminal-based Python application designed to help users build consistency, break bad habits, and track their daily progress. It is a beginner-friendly Python project that helps users track daily habits, mark completions, calculate streaks, and view progress statistics — all through a simple menu-driven console program.

-> Overview: Daily Habit Tracker helps users build consistency by creating personal habits, marking them complete each day, and automatically calculating current and longest streaks. The project is organized into separate Python modules, making the code user-friendly, readable, and easy to maintain or extend.

-> Note: This is an educational project that shows practical use of Python fundamentals like functions, modules, lists, dictionaries, input validation, conditionals, and loops. It is not a full productivity or health application.

-> Requirements
- Python 3.x
- No external Python packages or libraries are required.

-> Features  
1. Add, edit, and delete habits  
2. Mark a habit as completed for the current day  
3. Prevents marking the same habit twice on the same day  
4. Calculates current streak  
5. Calculates longest streak  
6. Shows completion count and completion rate  
7. Displays all habits in a clean table format  
8. Exports a simple text progress report  
9. Automatically saves all data in a JSON file

-> Technologies / Tools Used  
1. Python 3  
2. json, os, datetime (standard libraries only)  
3. Git & GitHub (version control)

-> Project Structure  
|—> main.py               
|—> config.py            
|—> data_handler.py       
|—> habit_manager.py     
|—> streak_calculator.py 
|—> reporter.py            
|—> habits.json           
|—> README.md  
|—> statement.md

-> How to Run  
1. Keep all the .py files in the same folder  
2. Open a terminal in that folder  
3. Run the command: python main.py  
4. Follow the on-screen menu to use the application

-> Testing  
The application can be tested manually. Add a few habits and mark them complete on consecutive days to verify that current streak and longest streak are calculated correctly. Try editing and deleting habits to confirm changes are saved. Attempt to mark the same habit complete twice on the same day to check that duplicates are rejected. Close and reopen the program to ensure data persists. Finally, export the report and open the generated text file to verify its contents. Edge cases such as an empty habit list and invalid menu choices should also be tested.

->SCREENSHOTS
Main Menu
<img width="1920" height="1080" alt="Screenshot 2026-09-27 225925" src="https://github.com/user-attachments/assets/35a9a2c7-70b2-4adf-993c-b2afd78adff9" />
1.Add New Habit
<img width="1917" height="1017" alt="Screenshot 2026-09-27 230750" src="https://github.com/user-attachments/assets/f91b4089-b113-4696-a9b2-4af7062a5d86" />
2.View All Habits
<img width="1917" height="1020" alt="Screenshot 2026-09-27 231636" src="https://github.com/user-attachments/assets/18072155-60d3-44e7-95ba-415d2cc70d73" />
3.Edit Habit 
<img width="1917" height="1016" alt="Screenshot 2026-09-27 232002" src="https://github.com/user-attachments/assets/753bba56-a750-4722-86d1-a148a55fe7d7" />
4.Delete Habit
<img width="1917" height="1017" alt="Screenshot 2026-09-27 232345" src="https://github.com/user-attachments/assets/a715192f-6fac-4d76-bd86-02fb011b7346" />
5.Mark Habit Complete 
<img width="1917" height="1017" alt="Screenshot 2026-09-27 232542" src="https://github.com/user-attachments/assets/ba9f3357-d4c3-4038-b818-dc6a583daae2" />
6.View Statistics and Streaks
<img width="1917" height="1018" alt="Screenshot 2026-09-27 232630" src="https://github.com/user-attachments/assets/066599f2-80cf-448d-aa71-99e3ba2e49d1" />
<img width="1917" height="1020" alt="Screenshot 2026-09-27 232650" src="https://github.com/user-attachments/assets/c1b2ad65-d879-4abf-9cb9-b50e5d3f5247" />
7.Export Report
<img width="1917" height="1021" alt="Screenshot 2026-09-27 232728" src="https://github.com/user-attachments/assets/f5e168af-d854-41f1-b9aa-bdc7928fce0f" />
0.Exit 
<img width="1917" height="1020" alt="Screenshot 2026-09-27 232826" src="https://github.com/user-attachments/assets/66e7910c-627c-4c1d-a847-4e2ac1d8928f" />
Github
<img width="1917" height="968" alt="Screenshot 2026-09-28 001955" src="https://github.com/user-attachments/assets/f2edbe68-50ea-4679-a711-a05f298614dd" />














