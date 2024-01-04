class TaskList:  #Criação de uma classe 
    def __init__(self):
        self.tasks = []  #Array que irá guardar as tarefas da lista

    def add_task(self, task, description):  #function that adds a task and its description to the task list 
        self.tasks.append({'task': task, 'description': description})

    def view_tasks(self): #function responsible for the visualization of the task list
        if not self.tasks: #in case there are no tasks
            print("No tasks found.")
        else: #in case there are tasks
            print("Task List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task['task']}: {task['description']}")

    def edit_task(self, task_index, task_name, task_description): #function responsible for editing an already existing task
        if 1 <= task_index <= len(self.tasks):
            edit_task = self.tasks[task_index - 1] #task to be edited
            edit_task['task'] = task_name
            edit_task['description'] = task_description
            print("Edited task:")
            print(f"{task_index}. {edit_task['task']}: {edit_task['description']}")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks.pop(task_index - 1)
            print(f"Task {task_index} removed.")
        else:
            print("Invalid task index.")


def main():
    task_list = TaskList() #task_list is now a TaskList class object

    while True: #Command Line Interface
        print("\nTask List Menu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Remove Task")
        print("4. View Tasks")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task name: ")
            description = input("Enter its description: ")
            task_list.add_task(task, description)
            print("Task added successfully.")
        elif choice == '2':
            task_index = input("Enter the task index: ")
            task_name = input("Edit task name: ")
            task_description = input("Edit task description: ")
            task_list.edit_task(int(task_index), task_name, task_description)
            print("Task edited successfully.")
        elif choice == '3':
            task_index = int(input("Enter the task index: "))
            task_list.remove_task(task_index)
            print("Task removed successfully.")
        elif choice == '4':
            task_list.view_tasks()
        elif choice == '5':
            print("Exiting the task list.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":  #Executes the programs main function
    main()
