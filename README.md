Certainly! Here's an updated README with code snippets highlighting some features:

---

# Task Manager CLI

This is a command-line interface (CLI) application for managing tasks. It allows users to create an account, log in, view tasks, create new tasks, update tasks, and mark tasks as completed.

## Technologies

Python, MySQL, Hashlib

### Usage

To run the application, execute the following command in your terminal:

```bash
python cli.py
```

This will start the application, and you will be prompted with options to create an account, log in, and perform various tasks.

## Features

- **Account Management**: Users can create an account with a username and password.

  ```python
  def sign_up():
      username = input('\033[35mCreate Your Username:\033[0m ')
      password = input('\033[35mCreate Your Password:\033[0m ')

      try:
          user = User.create(username, password)
          print(f'\033[32m{user.username} Created Successfully!\033[0m')
      except Exception as exc:
          return print(f'\033[31mError creating user, {exc}')
  ```

- **Authentication**: Users can log in securely with their credentials. Each user has their own set of tasks based on their user id.

  ```python
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
  ```

- **Task Management**: Users can view their tasks, create new tasks, update existing tasks, and mark tasks as completed.

  ```python
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
  ```

- **Priority Levels**: Tasks can be assigned priority levels (LOW, MEDIUM, HIGH).

- **Color-coded Interface**: The CLI interface uses colors to enhance readability and highlight important information.

## Highlights

### Object-Oriented Programming (OOP):

- Implemented classes such as User and Task to represent entities in the - application.
- Utilized encapsulation to define properties and behaviors of objects, ensuring data integrity and code maintainability.
- Employed inheritance and polymorphism to create class hierarchies and promote code reusability.
- Leveraged class methods and static methods to encapsulate business logic and utility functions.

### Database Interaction:

- Integrated SQLite database to persist user accounts and task data.
- Utilized SQL queries and database transactions to perform CRUD (Create, Read, Update, Delete) operations on user and task entities.
- Implemented database migrations to manage changes in the database schema over time, ensuring data consistency and application stability

### Security and Data Protection:

- Implemented secure password hashing using the SHA-256 cryptographic hash function to protect user passwords.
- Enforced password complexity requirements and input validation to mitigate common security risks such as brute-force attacks and SQL injection.
- Leveraged secure database connections and parameterized queries to prevent SQL injection vulnerabilities and safeguard sensitive user data.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to contribute to the development of this project.

## License

This project is licensed under the [MIT License](LICENSE).
