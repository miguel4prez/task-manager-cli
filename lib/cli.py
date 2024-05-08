# lib/cli.py

from helpers import (
    exit_program,
    sign_up,
    log_in,
    view_tasks,
    create_task,
    update_task,
    complete_task
)

def main():
    user = None

    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            sign_up()
        elif choice == "2":
            user = log_in()
            if user:
                break
        else:
            print("\033[31mInvalid choice\033[0m")

    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            view_tasks(user.id)
        elif choice == "2":
            if user: 
                create_task(user)
        elif choice == "3":
            if user:
                update_task(user.id)
        elif choice == "4":
            if user:
                complete_task(user.id)
        elif choice == "5":
            exit_program()
        else:
            print("\033[31mInvalid choice\033[0m")


def main_menu():
    print("\033[35mPlease select an option:\033[0m")
    print("0. Exit the program")
    print("1. Create an account")
    print("2. Log In")

def menu():
    print("\033[35mPlease select an option:\033[0m")
    print("0. Exit the program")
    print("1. View your tasks")
    print("2. Create a new task")
    print("3. Update a task")
    print("4. Complete Task")
    print("5. Log Out")


if __name__ == "__main__":
    main()
