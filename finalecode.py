from datetime import datetime

class Task:
    task_id_counter = 1

    def __init__(self, title, description, priority, date):
        self.task_id = Task.task_id_counter
        self.title = title
        self.description = description
        self.priority = priority
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.isCompleted = False
        Task.task_id_counter += 1

    def getID(self):
        return self.task_id

    def __str__(self):
        return f"Task ID: {self.task_id}\nTitle: {self.title}\nDescription: {self.description}\nPriority: {self.priority}\nDate: {self.date.strftime('%Y-%m-%d')}\n"


class TaskManager:
    def __init__(self):
        self.tasksList = []
        self.overdueTasksList = []  # Added a separate list for overdue tasks
        self.finishedTasksList = []

    def getTasksList(self):
        return self.tasksList

    def getOverdueTasksList(self):
        return self.overdueTasksList

    def getFinishedTasksList(self):
        return self.finishedTasksList

    def addTask(self, title, description, priority, date):
        task = Task(title, description, priority, date)
        self.tasksList.append(task)

    def findTaskByID(self, ID):
        for task in self.tasksList:
            if task.getID() == ID:
                return task
        return None

    def removeTaskLiteral(self, task):
        if task in self.tasksList:
            self.finishedTasksList.append(task)
            self.tasksList.remove(task)
        elif task in self.overdueTasksList:
            self.overdueTasksList.remove(task)
        else:
            print("Tried to remove a task that does not exist:", task)

    def removeTaskByID(self, ID):
        task = self.findTaskByID(ID)
        if task is not None:
            self.removeTaskLiteral(task)
            self.resetTaskIDCounter()
        else:
            print("Failed to locate a task based on the ID passed in:", ID)

    def resetTaskIDCounter(self):
        if self.getFinishedTasksList():
            max_id = max(task.getID() for task in self.getFinishedTasksList())
            Task.task_id_counter = max_id + 1
        else:
            Task.task_id_counter = 1

    def completeTask(self, task):
        task.isCompleted = True
        self.finishedTasksList.append(task)
        self.removeTaskLiteral(task)
        self.resetTaskIDCounter()

    def taskOverdue(self, task):
        if not task.isCompleted:
            try:
                current_date = datetime.now()
                return task.date < current_date
            except ValueError:
                print("Error comparing dates.")
        return False

    def checkOverdueTasks(self):
        for task in self.getTasksList():
            overdue = self.taskOverdue(task)
            if overdue:
                print("Task", task, "is overdue!")
                self.overdueTasksList.append(task)

    def printManager(self):
        for i in self.tasksList:
            print(i)

    def printOverdueTasks(self):
        for task in self.overdueTasksList:
            print(task)

    def printFinished(self):
        for task in self.finishedTasksList:
            print(task)

    def remainingTimeForTask(self, task):
        remaining_time = task.date - datetime.now()
        return str(remaining_time)

#########################################################################################################################################

def case1():
    title = input("Enter a title for your task: ")
    description = input("Write a brief description of your task: ")
    priority = int(input("Select the level of priority of your task on a scale of 1 to 3, with 3 being the highest level of priority: "))
    date = input("Enter the due date of this task (YYYY-MM-DD): ")
    task_manager.addTask(title, description, priority, date)

def case2():
    ID = int(input("Enter the ID of the task you want to remove: "))
    task_manager.removeTaskByID(ID)
    print(f"Task with ID: {ID} was removed.")

def case3():
    tasks = task_manager.getTasksList()
    for task in tasks:
        print(task)

def case4():
    task_manager.printFinished()

def case5():
    task_manager.checkOverdueTasks()

def case6():
    taskID = int(input('Enter the ID of the Task you are searching for: '))
    task = task_manager.findTaskByID(taskID)
    if task is not None:
        print(task)
    else:
        print(f"No task found with ID: {taskID}")

def case7():
    taskID = int(input('Enter the ID of the Task you are searching for: '))
    task = task_manager.findTaskByID(taskID)
    if task is not None:
        remaining_time = task_manager.remainingTimeForTask(task)
        print(f"Time remaining for Task {taskID}: {remaining_time}")
    else:
        print(f"No task found with ID: {taskID}")


def case8():
    taskID = int(input('Enter the ID of the Task you want to mark as completed: '))
    task = task_manager.findTaskByID(taskID)
    if task is not None:
        task_manager.completeTask(task)
        print(f"Task with ID: {taskID} marked as completed.")
    else:
        print(f"No task found with ID: {taskID}")

def case9():

    task_manager.printOverdueTasks()

def case10():
    print("Exiting the program.")
    exit()

switch = {1: case1, 2: case2, 3: case3, 4: case4, 5: case5, 6: case6, 7: case7, 8: case8, 9:case9, -1: case10}
commandlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "-1"]

def main():
    while True:
        command = ''
        while not command in commandlist:
            command = input("MENU:\n"
                            "Press 1 to add a new Task\n"
                            "Press 2 to remove a Task\n"
                            "Press 3 to show all Tasks\n"
                            "Press 4 to show completed Tasks\n"
                            "Press 5 to show overdue tasks\n"
                            "Press 6 to find a task by ID\n"
                            "Press 7 to show remaining time for a task\n"
                            "Press 8 to mark a task as completed\n"
                            "Press -1 to close the program\n"
                            "What action would you like to perform?: "
                            "")
        command = int(command)

        if command == -1:
            print("Exiting the program")
            break

        if command in switch:
            switch[command]()
        else:
            print("You should enter either 1, 2, 3, 4, 5, 6, 7, or -1.")
            print("\n")

if __name__ == "__main__":
    task_manager = TaskManager()
    main()
