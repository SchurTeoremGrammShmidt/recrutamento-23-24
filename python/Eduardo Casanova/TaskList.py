import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMessageBox, QPushButton, QLineEdit, QListWidget, QLabel, QCalendarWidget, QInputDialog, QDateTimeEdit
from PyQt5.QtCore import QDateTime

# Class definition for TaskManager
class TaskManager(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        # Initialize lists to store tasks and their string representations
        self.tasks = []
        self.task_overviews = []

        # Get the current date and time
        self.current_time = QDateTime.currentDateTime()
        
        # Initialize the UI and get the selected date
        self.current_date = self.start_ui()
        

    # Method to set up the UI
    def start_ui(self):
        
        # Create a vertical layout for the UI
        layout = QVBoxLayout()
        
        # Create buttons for adding, deleting, and viewing tasks
        add_button = QPushButton('Add Task', self)
        add_button.clicked.connect(self.add_task)
        
        delete_button = QPushButton('Delete Task', self)
        delete_button.clicked.connect(self.delete_task)
        
        details_button = QPushButton('Details', self)
        details_button.clicked.connect(self.delete_task)  # Note: This currently connects to the delete_task method, should be corrected
        
        # Create a list widget to display tasks
        self.task_list = QListWidget(self)
        
        # Create a calendar widget and a time editor
        self.calendar = QCalendarWidget(self)
        self.time_edit = QDateTimeEdit(self)
        self.time_edit.setDisplayFormat("HH:mm")  
        self.time_edit.setDateTime(self.current_time)
        
        # Add widgets to the layout
        layout.addWidget(add_button)
        layout.addWidget(self.task_list)
        layout.addWidget(details_button)
        layout.addWidget(delete_button)
        layout.addWidget(self.calendar)
        layout.addWidget(self.time_edit)
        
        # Set the layout for the widget and display it
        self.setLayout(layout)
        self.show()
        
        # Return the selected date from the calendar
        return self.calendar.selectedDate()  # Get today's date

    # Method to add a new task
    def add_task(self):
        
        # Update current time to the current date and time
        self.current_time = QDateTime.currentDateTime()
        
        # Get the current date
        current_date = self.current_time.date()
        
        # Get the selected date from the calendar and time from the time editor
        date = self.calendar.selectedDate()
        time = self.time_edit.time()
        
        # Check if the selected date is in the past
        if date < current_date:
            # Display an error message if the date is in the past
            msg = QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('The day you picked is long gone :(')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return
            
        # Prompt the user to enter task name and description
        title, done1 = QInputDialog.getText(self, 'Task Name', 'Enter Task Name...')
        desc, done2 = QInputDialog.getText(self, 'Task Description', 'Enter Task Description...')
        
        # Check if both task name and description are provided
        if done1 and done2 :
            # Create a new Task instance
            task = Task(title, desc, date, time)
            
            # Create a string representation of the task
            title_string = task.title + '\n' + task.getDateString()
            
            # Add the task to the lists and update the task list
            self.tasks.append(task) 
            self.task_overviews.append(title_string)
            self.update_task_list()
        else:
            print('Invalid Task')
        return

    # Method to delete a task
    def delete_task(self):
        
        # Get the currently selected item in the task list
        selected_item = self.task_list.currentItem()
        
        # Check if an item is selected
        if selected_item:
            # Get the text of the selected item
            task_text = selected_item.text()
            
            # Remove the task from the task_overviews list
            self.task_overviews.remove(task_text)
            
            # Iterate through tasks to find and remove the corresponding task instance
            for task in self.tasks:
                if task.overview == task_text:
                    self.tasks.remove(task)
            
            # Update the task list
            self.update_task_list()
        return

    # Method to update the task list
    def update_task_list(self):

        # Clear the task list widget
        self.task_list.clear()
        
        # Sort the tasks using bubble sort
        self.bubbleSort()
        
        i = 0
        
        # Iterate through sorted tasks and update task_overviews list
        for task in self.tasks:
            self.task_overviews[i] = task.overview
            i = i + 1
        
        # Add the updated task_overviews list to the task list widget
        self.task_list.addItems(self.task_overviews)

    # Method to implement the bubble sort algorithm for sorting tasks by date and time
    def bubbleSort(self):
        
        n = len(self.tasks)
        swapped = False

        for i in range(n-1):

            for j in range(0, n-i-1):
                
                # Compare tasks based on date and time, swap if necessary
                if (self.tasks[j].date > self.tasks[j + 1].date) or (self.tasks[j].date == self.tasks[j + 1].date and self.tasks[j].time > self.tasks[j + 1].time):
                    swapped = True
                    self.tasks[j], self.tasks[j + 1] = self.tasks[j + 1], self.tasks[j]
            
            # If no swaps occurred in a pass, the list is already sorted
            if not swapped:
                return
    
# Class definition for Task
class Task():
    
    # Constructor to initialize task attributes
    def __init__(self, title, desc, date, time):
        
        self.title = title
        self.desc  = desc
        self.date  = date
        self.time  = time
        # Create a string representation of the task
        self.overview = self.title + '\n' + self.getDateString() + '  ' + self.getTimeString()

    # Method to get a formatted string of the task date
    def getDateString(self):
        date = str(self.date.day()) + '-' + str(self.date.month()) + '-' + str(self.date.year())
        return date

    # Method to get a formatted string of the task time
    def getTimeString(self):
        time = str(self.time.hour()) + ':' + str(self.time.minute())
        return time

# Application entry point
if __name__ == '__main__':
    # Create a PyQt application
    app = QApplication(sys.argv)
    
    # Set the application style to 'Fusion'
    app.setStyle('Fusion')
    
    # Create an instance of TaskManager
    task_manager = TaskManager()
    
    # Start the application event loop
    sys.exit(app.exec_())
