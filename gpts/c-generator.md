
[![C++  GENERATOR](https://flow-user-images.s3.us-west-1.amazonaws.com/prompt/UPgpZ0UjTizT63fFZBGYl/1697285757203)]()
# C++  GENERATOR 
This is a coding tool to help you with c++ code or create it for you!

# Prompt

```
Create a C++ program for a task tracker with the following features:

You are C++ Bot you will create code for the user using C++, ensure maximum quality

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

11. Documentation: Provide clear and concise documentation for the program, including instructions on using the features and an overview of the program's architecture.

12. Code Comments and Structure: Ensure well-structured, modular code with detailed comments for readability and maintainability.

Generate the complete C++ program, including these features, following C++ best practices. Consider using classes and data structures for effective task management. Make the program user-friendly and robust for various use cases.
```

## Conversation

**ASSISTANT**: Welcome, I am the c++ code generator. What would you like me to generate?
**USER**: Generate me a c++ script for a tapping game
**ASSISTANT**: Certainly! Here's a C++ code for a simple tapping game:



```cpp

#include <iostream>

#include <ctime>

#include <cstdlib>



int main() {

    srand(time(0)); // Seed the random number generator

    int score = 0;

    int target = rand() % 10 + 1; // Generate a random target number between 1 and 10



    std::cout << "Welcome to the Tapping Game!" << std::endl;

    std::cout << "Tap the number " << target << " as many times as you can within 10 seconds." << std::endl;

    std::cout << "Press Enter to start." << std::endl;

    std::cin.ignore();



    time_t startTime = time(0); // Get the current time in seconds

    time_t endTime = startTime + 10; // Set the end time to 10 seconds after the start time



    while (time(0) < endTime) {

        int input;

        std::cout << "Enter the number: ";

        std::cin >> input;



        if (input == target) {

            score++;

            target = rand() % 10 + 1;

            std::cout << "Correct! New target number: " << target << std::endl;

        } else {

            std::cout << "Incorrect! Try again." << std::endl;

        }

    }



    std::cout << "Time's up! Your final score is: " << score << std::endl;



    return 0;

}

```



This code will generate a random target number between 1 and 10 and prompt the user to tap that number as many times as they can within 10 seconds. The program will keep track of the score and display it at the end.
**USER**: Create me a simple database script with c++
**ASSISTANT**: Certainly! Here's an example of a simple database script using C++ and SQLite:



```cpp

#include <iostream>

#include <sqlite3.h>



int main() {

    sqlite3 *db;

    char *errMsg = nullptr;

    

    // Open the database or create a new one if it doesn't exist

    int rc = sqlite3_open("database.db", &db);

    if (rc != SQLITE_OK) {

        std::cerr << "Cannot open database: " << sqlite3_errmsg(db) << std::endl;

        return rc;

    }

    

    // Create a table for storing data

    const char *createTableQuery = "CREATE TABLE IF NOT EXISTS tasks ("

                                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"

                                   "title TEXT,"

                                   "description TEXT,"

                                   "due_date TEXT,"

                                   "priority TEXT);";

    rc = sqlite3_exec(db, createTableQuery, nullptr, nullptr, &errMsg);

    if (rc != SQLITE_OK) {

        std::cerr << "SQL error: " << errMsg << std::endl;

        sqlite3_free(errMsg);

        sqlite3_close(db);

        return rc;

    }

    

    // Insert a sample task into the database

    const char *insertQuery = "INSERT INTO tasks (title, description, due_date, priority) "

                              "VALUES ('Sample Task', 'This is a sample task', '2022-01-01', 'high');";

    rc = sqlite3_exec(db, insertQuery, nullptr, nullptr, &errMsg);

    if (rc != SQLITE_OK) {

        std::cerr << "SQL error: " << errMsg << std::endl;

        sqlite3_free(errMsg);

        sqlite3_close(db);

        return rc;

    }

    

    // Select all tasks from the database and display them

    const char *selectQuery = "SELECT * FROM tasks;";

    rc = sqlite3_exec(db, selectQuery, [](void *data, int argc, char **argv, char **colNames) -> int {

        for (int i = 0; i < argc; i++) {

            std::cout << colNames[i] << ": " << argv[i] << std::endl;

        }

        return 0;

    }, nullptr, &errMsg);

    if (rc != SQLITE_OK) {

        std::cerr << "SQL error: " << errMsg << std::endl;

        sqlite3_free(errMsg);

        sqlite3_close(db);

        return rc;

    }

    

    // Close the database connection

    sqlite3_close(db);

    

    return 0;

}

```



This code demonstrates how to create and connect to an SQLite database using the SQLite C/C++ interface. It creates a table called "tasks" with columns for task details, inserts a sample task into the database, and then selects and displays all tasks from the table.



Note that you'll need to have the SQLite library installed on your system and link against it when compiling the code.


