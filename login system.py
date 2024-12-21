# Initialize a dictionary to store user credentials
users = {
    "admin": "password",
    "user": "password123",
}
def register():
    """Register a new user"""
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Check if username already exists
    if username in users:
        print("Username already exists. Please try again.")

    else:
        users[username] = password
        print("User registered successfully!")


def login():
    """Login to the system"""
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if username and password match
    if username in users and users[username] == password:
        print("Login successful! Welcome, " + username)
    else:
        print("Invalid username or password. Please try again.")


def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
