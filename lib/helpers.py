
from models.user import User
from models.task import Task

def exit_program():
    print("Goodbye!")
    exit()

def sign_up():
    username = input('Create Your Username: ')
    password = input('Create Your Password: ')

    try:
        user = User.create(username, password)
        print(f'{user.username} Created Successfully!')
    except Exception as exc:
        return print(f'Error creating user, {exc}')
    
def log_in():
    username = input('Enter Your Username: ')
    password = input('Enter Your Password: ')

    user = User.find_by_username(username)

    if user:
        if password == user.password:
            print(f'Welcome {user.username}!')
            return True
        else:
            print('Invalid Password')
    else:
        print('User does not exist')
    return False


def view_tasks():
    tasks = Task.view_all()

    if tasks:
        # print(f'{tasks.task_name}, priotiy: {tasks.priority}')
        print(f'{tasks}')
    else:
        print('You have no tasks')

def create_task():
    task_name = input('Name of task: ')

    priority = input('Priority Level: [HIGH] - [MEDIUM] - [LOW] > ')

    try:
        task = Task.create(task_name, priority)
        print(f'Task {task.id} has been created!')
    except Exception as exc:
        return print(f'Error creating task', {exc})

    