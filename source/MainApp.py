from User import *

class MainApp(object):

    def __init__(self):
        self.activeuser = None
        self.users = []

    def start(self):
        print("---APP STARTED---\n-Press Q to Quit-")
        while True:
            print("Option:")
            print("1. Login")
            print("2. Register")
            userinp = str(input("Select: "))

            if userinp == "Q":
                break
            elif userinp == "1":
                self.performLogin()
            elif userinp == "2":
                self.performRegistration()

    def getUserObjectByName(self, name):
        for user in self.users:
            if user.name == name:
                return user;
        return -1;

    def performLogin(self):
        name = str(input("Your name: "))
        if self.isRegistered(name):
            self.doLogin(self.getUserObjectByName(name))
        else:
            print("You are not registered, are you?");

    def isRegistered(self, name):
        find = False
        for user in self.users:
            if user.name == name:
                find = True
        return find

    def doLogin(self, user):
        self.activeuser = user
        self.usermenu()
    
    def performRegistration(self):
        print("Register")
        while True:
            name = str(input("Your name: "))
            if self.isRegistered(name):
                print("Name's taken, cuh!")
            else:
                break;
        age = int(input("Your age: "))
        newuser = User(name, age)
        self.users.append(newuser)
        print("Horray, your account has been created!")
        self.activeuser = newuser
        self.usermenu()

    def usermenu(self):
        while True:
            print("Option:\n1. Add a friend\n2. List of my friends\n3. Delete a friend\n4. Log out");
            userinp = str(input("Select: "))
            if userinp == "1":
                pass;
            if userinp == "2":
                pass;
            if userinp == "3":
                pass;
            if userinp == "4":
                self.activeuser = None;
                break;
            if userinp == "Q":
                exit(0)

if __name__ == "__main__":
    app = MainApp()
    app.start()
















