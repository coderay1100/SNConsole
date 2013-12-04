# File: User.py
# -------------
# This class defines User object.

class User(object):

    # Constructor
    def __init__(self, name, age):
        # Initialize instance (object) properties
        self.name = name
        self.age = age
        self.friendList = []

    # Accessor/getter methods
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def printFriends(self):
        for user in self.friendList:
            print(user.getName())

    # Mutator/setter methods
    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age
    
    # Method for adding friend
    def addFriend(self, friend):
        self.friendList.append(friend)
        friend.receiveFriend(self)
    
    # Method for receiving friend request
    def receiveFriend(self, friend):
        self.friendList.append(friend)
