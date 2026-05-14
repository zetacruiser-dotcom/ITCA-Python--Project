import os
from datetime import datetime

USER_FILE = os.path.join(os.path.dirname(__file__), 'user_info.txt')

User_info = [
    {"username": "admin", "password": "admin123", "date_of_birth": "01/01/1990", "email": "Jordzz90@gmail.com",
     "phone_number": "1234567890", "last_login": "2024-06-01 10:00:00"},
    {"username": "Emily", "password": "user123", "date_of_birth": "15/05/1995", "email": "Emily234@gmail.com",
     "phone_number": "0987654321", "last_login": "2024-06-01 11:00:00"},
    {"username": "Michael", "password": "pass456", "date_of_birth": "20/08/1985", "email": "Michael567@gmail.com",
     "phone_number": "1122334455", "last_login": "2024-06-01 12:00:00"}
]

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_users(users, filename=USER_FILE):
    with open(filename, "w", encoding="utf-8") as file:
        for user in users:
            file.write(f"Username: {user['username']}\n")
            file.write(f"Password: {user['password']}\n")
            file.write(f"Date of Birth: {user['date_of_birth']}\n")
            file.write(f"Email: {user['email']}\n")
            file.write(f"Phone Number: {user['phone_number']}\n")
            file.write(f"Last Login: {user['last_login']}\n")
            file.write("\n")  # Add a blank line between users


def load_users(filename=USER_FILE):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        users = []
        blocks = content.strip().split("\n\n")
        for block in blocks:
            lines = block.split("\n")
            user = {}
            for line in lines:
                if ": " in line:
                    key, value = line.split(": ", 1)
                    key = key.lower().replace(" ", "_")
                    user[key] = value
            if user:
                users.append(user)
        return users
    except FileNotFoundError:
        return User_info  # fallback to hardcoded if no file

def add_user(users):
    print("\nAdd a new user")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    date_of_birth = input("Date of Birth (DD/MM/YYYY): ").strip()
    email = input("Email: ").strip()
    phone_number = input("Phone Number: ").strip()

    if not username or not password:
        print("Username and password are required.")
        return

    new_user = {
        "username": username,
        "password": password,
        "date_of_birth": date_of_birth,
        "email": email,
        "phone_number": phone_number,
        "last_login": get_current_time()
    }

    users.append(new_user)
    save_users(users)
    print(f"User '{username}' added and saved to user_info.txt.")


def login_user(users):
    print("\nUser login")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    for user in users:
        if user["username"] == username and user["password"] == password:
            user["last_login"] = get_current_time()
            save_users(users)
            print(f"Welcome back, {username}! Last login updated.")
            return

    print("Invalid username or password.")


def main_menu():
    global User_info
    User_info = load_users()  # load from file on startup
    while True:
        print("\n=== User Menu ===")
        print("1. Add new user")
        print("2. Login user")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_user(User_info)
            save_users(User_info)  # save after adding a user
        elif choice == "2":
            login_user(User_info)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option.")


if __name__ == "__main__":
    main_menu()
        
