# lib/cli.py

from helpers import (
    exit_program,
    sign_up,
    log_in,
    view_tasks,
    create_task
)

def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            sign_up()
        elif choice == "2":
            if log_in():
                break
        else:
            print("Invalid choice")

    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            view_tasks()
        elif choice == "2":
            create_task()


def main_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create an account")
    print("2. Log In")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. View your tasks")
    print("2. Create a new task")
    print("3. Update a task")
    print("4. Delete a task")


if __name__ == "__main__":
    main()
