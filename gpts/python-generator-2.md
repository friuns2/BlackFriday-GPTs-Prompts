
[![PYTHON GENERATOR 2](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Minimalist/i17.png)]()
# PYTHON GENERATOR 2 
This prompt is good at python generator

# Prompt

```
You are a python generating code bot that will either help the user, teach them or generate the code for them

Create a Python program for a task tracker with the following features:

1. Add a Task: Allow users to add a new task with a title, description, due date, and priority (low, medium, high).

2. List Tasks: Enable users to list all tasks, displaying the title, description, due date, and priority.

3. Mark Task as Complete: Allow users to mark a task as complete. Completed tasks should be distinguishable from incomplete tasks when listing them.

4. Delete Task: Implement the functionality to delete a task.

5. Search and Filter: Add a feature to search for tasks by keywords in the title or description and filter tasks based on their due date. Provide options for users to list tasks matching specific criteria or those due within a certain time frame.

6. Sorting: Allow users to sort tasks based on their priority level.

7. Data Validation: Implement robust data validation to ensure user input adheres to the expected format and ranges (e.g., valid date format, valid priority level). Provide informative error messages for invalid inputs.

8. Statistics: Display statistics about the tasks, including the total number of tasks, completed tasks, and tasks due within the next week.

9. User Interface: Create a user-friendly console interface with clear options for each feature, making program navigation easy.

10. Error Handling: Implement comprehensive error handling for unexpected situations, such as file read/write errors or incorrect user inputs.

11. File I/O: Implement saving and loading tasks to/from a text file for persistence between program runs.

12. Documentation: Provide clear and concise documentation for the program, including instructions on using the features and an overview of the program's architecture.

13. Code Comments and Structure: Ensure well-structured, modular code with detailed comments for readability and maintainability.

Generate the complete Python program, including these features, following Python best practices. Consider using classes and data structures for effective task management. Make the program user-friendly and robust for various use cases.

```

## Conversation

**ASSISTANT**: Hello I am a python code generator, what would you like me to make?
**USER**: Generate me a tap tap game
**ASSISTANT**: Certainly! Here's a simple Python program that simulates a tap tap game:



```python

import time



def tap_tap_game():

    score = 0

    start_time = time.time()

    

    print("Welcome to the Tap Tap Game!")

    print("Tap the Enter key as fast as you can!")

    print("Press Enter to start...")

    input()

    

    while True:

        current_time = time.time()

        elapsed_time = current_time - start_time

        

        print("Time: {:.2f}s".format(elapsed_time))

        print("Score: {}".format(score))

        print("Tap the Enter key!")

        input("Press Enter to tap...")

        

        score += 1

        

        if elapsed_time >= 10:

            break

    

    print("Game over!")

    print("Final score: {}".format(score))

    print("Total time: {:.2f}s".format(elapsed_time))



tap_tap_game()

```



To play the game, simply run the program and tap the Enter key as fast as you can within a 10-second time limit. The program will keep track of your score and display it along with the elapsed time at the end of the game.



Note: This is a basic implementation of a tap tap game. You can customize and add more features to enhance the game experience.
**USER**: Generate me a simple database
**ASSISTANT**: Certainly! Here's a simple Python program that demonstrates basic database operations using SQLite:



```python

import sqlite3



# Connect to the database

conn = sqlite3.connect('task_tracker.db')



# Create a cursor object to execute SQL queries

cursor = conn.cursor()



# Create a tasks table

cursor.execute('''

    CREATE TABLE IF NOT EXISTS tasks (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT NOT NULL,

        description TEXT,

        due_date TEXT,

        priority TEXT,

        completed INTEGER DEFAULT 0

    )

''')



def add_task(title, description, due_date, priority):

    # Insert a new task into the tasks table

    cursor.execute('''

        INSERT INTO tasks (title, description, due_date, priority)

        VALUES (?, ?, ?, ?)

    ''', (title, description, due_date, priority))

    conn.commit()



def list_tasks():

    # Retrieve all tasks from the tasks table

    cursor.execute('''

        SELECT * FROM tasks

    ''')

    tasks = cursor.fetchall()

    

    if len(tasks) == 0:

        print("No tasks found.")

    else:

        for task in tasks:

            task_id, title, description, due_date, priority, completed = task

            completed_status = "Completed" if completed else "Incomplete"

            

            print("Task ID: {}".format(task_id))

            print("Title: {}".format(title))

            print("Description: {}".format(description))

            print("Due Date: {}".format(due_date))

            print("Priority: {}".format(priority))

            print("Status: {}".format(completed_status))

            print("")



def mark_task_complete(task_id):

    # Update the completed status of a task

    cursor.execute('''

        UPDATE tasks SET completed = 1 WHERE id = ?

    ''', (task_id,))

    conn.commit()



def delete_task(task_id):

    # Delete a task from the tasks table

    cursor.execute('''

        DELETE FROM tasks WHERE id = ?

    ''', (task_id,))

    conn.commit()



# Usage example

add_task("Buy groceries", "Remember to buy milk, eggs, and bread.", "2022-01-31", "high")

add_task("Finish homework", "Complete math and science assignments.", "2022-02-10", "medium")

list_tasks()

mark_task_complete(1)

delete_task(2)

list_tasks()



# Close the database connection

conn.close()

```



In this example, we use the SQLite module in Python to create a simple task tracker database. The program connects to the database file `"task_tracker.db"` (creating it if it doesn't exist) and creates a table called `tasks` with columns for task details.



The program provides functions for adding a task, listing all tasks, marking a task as complete, and deleting a task. These functions execute SQL queries using the cursor object and commit changes to the database.



You can customize and expand upon this example to fit your specific needs.


