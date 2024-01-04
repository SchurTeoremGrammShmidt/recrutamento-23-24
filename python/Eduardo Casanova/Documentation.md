
# Task Manager Documentation

## Overview

The provided code is a simple task manager application built using PyQt5, a Python library for creating desktop applications with graphical user interfaces (GUI). The task manager allows users to add tasks, view task details, and delete tasks. Tasks are displayed in a list, sorted by date and time. The application uses the Qt framework for its UI components.

## Classes

### 1. `TaskManager` Class

#### Attributes

-   `tasks`: A list to store instances of the `Task` class, representing individual tasks.
-   `task_overviews`: A list to store string representations of task details for display in the task list.
-   `current_time`: Stores the current date and time.
-   `current_date`: Represents the date selected on the calendar in the UI.

#### Methods

-   `start_ui()`: Initializes the UI components and returns the selected date from the calendar.
-   `add_task()`: Adds a new task to the task list.
-   `delete_task()`: Deletes the selected task from the task list.
-   `update_task_list()`: Updates the task list with the current task information.
-   `bubbleSort()`: Implements the bubble sort algorithm to sort tasks by date and time.

### 2. `Task` Class

#### Attributes

-   `title`: Task title.
-   `desc`: Task description.
-   `date`: Task date.
-   `time`: Task time.
-   `overview`: String representation of the task for display.

#### Methods

-   `getDateString()`: Returns a formatted string of the task date.
-   `getTimeString()`: Returns a formatted string of the task time.

## UI Components

-   `QPushButton`: Buttons for adding tasks, deleting tasks, and viewing task details.
-   `QListWidget`: Displays the list of tasks.
-   `QCalendarWidget`: Allows users to select a date.
-   `QDateTimeEdit`: Allows users to select a time.

## Usage

1.  Run the script.
2.  The main window opens with buttons for adding, deleting, and viewing tasks, a task list, a calendar, and a time editor.
3.  Click "Add Task" to add a new task. Enter the task name and description when prompted.
4.  Select a date from the calendar and set the time using the time editor.
5.  Click "OK" to add the task or "Cancel" to discard.
6.  Tasks are displayed in the list, sorted by date and time.
7.  Click "Delete Task" to remove a selected task from the list.

## Notes

-   Tasks are sorted automatically based on their date and time.
-   An error message is displayed if the selected date is in the past when adding a new task.
-   Task details can be viewed by clicking the "Details" button (not fully implemented in the provided code).
-   The code uses a simple bubble sort algorithm for sorting tasks, and the sorting happens each time a task is added or deleted.# Task Manager Documentation

## Overview

The provided code is a simple task manager application built using PyQt5, a Python library for creating desktop applications with graphical user interfaces (GUI). The task manager allows users to add tasks, view task details, and delete tasks. Tasks are displayed in a list, sorted by date and time. The application uses the Qt framework for its UI components.

## Classes

### 1. `TaskManager` Class

#### Attributes

-   `tasks`: A list to store instances of the `Task` class, representing individual tasks.
-   `task_overviews`: A list to store string representations of task details for display in the task list.
-   `current_time`: Stores the current date and time.
-   `current_date`: Represents the date selected on the calendar in the UI.

#### Methods

-   `start_ui()`: Initializes the UI components and returns the selected date from the calendar.
-   `add_task()`: Adds a new task to the task list.
-   `delete_task()`: Deletes the selected task from the task list.
-   `update_task_list()`: Updates the task list with the current task information.
-   `bubbleSort()`: Implements the bubble sort algorithm to sort tasks by date and time.

### 2. `Task` Class

#### Attributes

-   `title`: Task title.
-   `desc`: Task description.
-   `date`: Task date.
-   `time`: Task time.
-   `overview`: String representation of the task for display.

#### Methods

-   `getDateString()`: Returns a formatted string of the task date.
-   `getTimeString()`: Returns a formatted string of the task time.

## UI Components

-   `QPushButton`: Buttons for adding tasks, deleting tasks, and viewing task details.
-   `QListWidget`: Displays the list of tasks.
-   `QCalendarWidget`: Allows users to select a date.
-   `QDateTimeEdit`: Allows users to select a time.

## Usage

1.  Run the script.
2.  The main window opens with buttons for adding, deleting, and viewing tasks, a task list, a calendar, and a time editor.
3.  Click "Add Task" to add a new task. Enter the task name and description when prompted.
4.  Select a date from the calendar and set the time using the time editor.
5.  Click "OK" to add the task or "Cancel" to discard.
6.  Tasks are displayed in the list, sorted by date and time.
7.  Click "Delete Task" to remove a selected task from the list.

## Notes

-   Tasks are sorted automatically based on their date and time.
-   An error message is displayed if the selected date is in the past when adding a new task.
-   Task details can be viewed by clicking the "Details" button (not fully implemented in the provided code).
-   The code uses a simple bubble sort algorithm for sorting tasks, and the sorting happens each time a task is added or deleted.
