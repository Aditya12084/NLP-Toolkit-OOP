import json

class UserManager:
    def __init__(self):
        self._database = {}
        self._load_database()

    def _load_database(self):
        try:
            with open("users.json", "r") as f:
                self._database = json.load(f)
        except FileNotFoundError:
            self._database = {}

    def _save_database(self):
        with open("users.json", "w") as f:
            json.dump(self._database, f)

    def register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email in self._database:
            print("Email already exists!")
            return False
        else:
            self._database[email] = [name, password]
            self._save_database()
            print("Registration successful.")
            return True

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email in self._database:
            if self._database[email][1] == password:
                print("Login successful.")
                return True
            else:
                print("Incorrect password.")
                return False
        else:
            print("Email not registered.")
            return False
