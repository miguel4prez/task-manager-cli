from models.user import User
from models.task import Task

def exit_program():
    print("\033[32mGoodbye!\033[0m")
    exit()

def sign_up():
    username = input('\033[35mCreate Your Username:\033[0m ')
    password = input('\033[35mCreate Your Password:\033[0m ')

    try:
        user = User.create(username, password)
        print(f'\033[32m{user.username} Created Successfully!\033[0m')
    except Exception as exc:
        return print(f'\033[31mError creating user, {exc}')
    
def log_in():
    username = input('\033[35mEnter Your Username:\033[0m ')
    password = input('\033[35mEnter Your Password:\033[0m ')

    user = User.find_by_username(username)

    if user:
        if password == user.password:
            print(f'\033[32mWelcome {user.username}!\033[0m')
            return user
        else:
            print('\033[31mInvalid Password\033[0m')
    else:
        print('\033[31mUser does not exist\033[0m')
    return False


def view_tasks(user_id):
    tasks = Task.view_all(user_id)
    task_color = None

    if tasks:
        for task in tasks:
            if task.priority == 'HIGH':
                task_color = "\033[31mHIGH\033[0m"
            elif task.priority == 'MEDIUM':
                task_color = "\033[33mMEDIUM\033[0m"
            elif task.priority == 'LOW':
                task_color = "\033[32mLOW\033[0m"
            print(f'Task {task.id}: \033[36m{task.task_name}\033[0m, Priority: {task_color}')
    else:
        print('\033[33mYou have no tasks\033[0m')


def create_task(user):
    task_name = input('\033[35mName of task:\033[0m ')

    while True:
        print("\033[35mPlease select priority level:\033[0m")
        print("\033[32m0. LOW\033[0m")
        print("\033[33m1. MEDIUM\033[0m")
        print("\033[31m2. HIGH\033[0m")

        choice = input('> ')
        if choice == '0':
            priority = 'LOW'
            break
        elif choice == '1':
            priority = 'MEDIUM'
            break
        elif choice == '2':
            priority = 'HIGH'
            break

    try:
        priority_level = ''.join(char for char in priority if char.isalnum())
        Task.create(task_name, priority_level, user.id)
        print(f'\033[32mTask has been created!\033[0m')
    except Exception as exc:
        return print(f'\033[31mError creating task\033[0m', {exc})
    
def update_task(user_id):
    tasks = Task.view_all(user_id)
    task_color = None

    if tasks:
        for task in tasks:
            if task.priority == 'HIGH':
                task_color = "\033[31mHIGH\033[0m"
            elif task.priority == 'MEDIUM':
                task_color = "\033[33mMEDIUM\033[0m"
            elif task.priority == 'LOW':
                task_color = "\033[32mLOW\033[0m"
            print(f'Task {task.id}: \033[36m{task.task_name}\033[0m, Priority: {task_color}')

        while True:
            edit_task = input('\033[35mSelect a task to edit:\033[0m ')
            if edit_task.isdigit():
                edit_task = int(edit_task)
                single_task = Task.find_by_id(edit_task)
                if single_task:
                    new_name = input('\033[35mUpdate the task name:\033[0m  ')
                    single_task.task_name = new_name

                    while True:
                        print("\033[35mPlease select priority level:\033[0m")
                        print("\033[32m0. LOW\033[0m")
                        print("\033[33m1. MEDIUM\033[0m")
                        print("\033[31m2. HIGH\033[0m")

                        choice = input('> ')
                        if choice == '0':
                            new_priority = 'LOW'
                            break
                        elif choice == '1':
                            new_priority = 'MEDIUM'
                            break
                        elif choice == '2':
                            new_priority = 'HIGH'
                            break

                    single_task.priority = new_priority

                    single_task.update()
                    print('\033[32mTask has been updated!\033[0m')
                    break
                else:
                    print('\033[31mInvalid task number\033[0m')
            else:
                print('\033[31mInvalid input. Please enter a number.\033[0m')
    else:
        print('\033[33mYou have no tasks\033[0m')
        

def complete_task(user_id):
    tasks = Task.view_all(user_id)
    task_color = None

    if tasks:
        for task in tasks:
            if task.priority == 'HIGH':
                task_color = "\033[31mHIGH\033[0m"
            elif task.priority == 'MEDIUM':
                task_color = "\033[33mMEDIUM\033[0m"
            elif task.priority == 'LOW':
                task_color = "\033[32mLOW\033[0m"
            print(f'Task {task.id}: \033[36m{task.task_name}\033[0m, Priority: {task_color}')

        while True:
            complete = input('\033[35mEnter the task number that you completed:\033[0m ')
            if complete.isdigit():
                complete = int(complete)
                single_task = Task.find_by_id(complete)
                if single_task:
                    single_task.delete()
                    print(f'\033[32m"{task.task_name}" Task Completed!\033[0m')
                    break
                else:
                    print('\033[31mInvalid task number\033[0m')
            else:
                print('\033[31mInvalid input. Please enter a number.\033[0m')
    else:
        print('\033[33mYou have no tasks\033[0m')





    