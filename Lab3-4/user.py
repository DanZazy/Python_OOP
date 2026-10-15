class User:

    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        print(f"This user: {self.first_name}, {self.last_name}")

    def greeting_user(self):
        print(f"Greetings, new user: {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts +=1
        print(f"Login attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login attempts: {self.login_attempts}")

