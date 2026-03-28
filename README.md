# Task Manager

## Project Overview
This is a Python-based command-line tool built to help students manage their daily workload. It was created as the **Bring Your Own Project (BYOP)** capstone for the VITyarthi course.

### Why this matters:
As a B.Tech student, I often have multiple assignments and lab records due at the same time. This tool provides a structured way to:
1. **Input** multiple tasks at once.
2. **Move** completed tasks from a "Pending" list to a "Done" list.
3. **View** a clear summary of current progress.

---

## Visual Walkthrough

### 1. Main Menu
The user is greeted with a clear menu of options:

<img width="954" height="175" alt="image" src="https://github.com/user-attachments/assets/bca00abd-cc82-4e65-8445-02c61ac42837" />


### 2. Adding Tasks
Users can add multiple tasks in a single session:

<img width="780" height="176" alt="image" src="https://github.com/user-attachments/assets/73274172-a048-4f39-824b-802ef1b031ca" />


### 3. Progress Tracking
A visual summary of what is pending and what is completed:

<img width="924" height="224" alt="image" src="https://github.com/user-attachments/assets/22388b41-9513-42d3-9240-1562ee899c7b" />


### 4. Completed Tasks
User can mark tasks as completed:

<img width="959" height="569" alt="image" src="https://github.com/user-attachments/assets/9e788fa3-5993-4efc-b94c-b9befbdb3ee2" />



---

## Features
* **Batch Addition:** Add multiple tasks in one go by specifying the count.
* **Status Tracking:** Automatically moves finished tasks to a "Completed" section.
* **Input Validation:** Checks if a task exists in the list before attempting to mark it as done.
* **Clean Interface:** Uses formatted separators like `========` to make the list easy to read.

---

## Tech Stack & Concepts Used
This project was built using **Python 3** and focuses on the following fundamental programming concepts:
* **Functions:** `add_task()`, `done_task()`, and `show()` keep the code modular.
* **Lists:** `todo_list` and `done_list` store the task data dynamically.
* **Loops:** A `while` loop runs the menu, and `for` loops iterate through the lists.
* **Conditional Logic:** `if-else` handles user choices and list verification.

---

## How to Run
1. Ensure you have **Python** installed.
2. Download the `task_manager.py` file.
3. Open your terminal or command prompt.
4. Run the script:
   ```bash
   python task_manager.py

---

