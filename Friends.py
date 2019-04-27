#File: Friends.py
#Description: HW 7
#Student's Name: Lisa Chu
#Student's UT EID: tc29328
#Course Name: CS 313E
#Unique Number: 50739
#
#Date Created: 4/10/19
#Date Last Modified: 4/11/19

#Defining node class for linked lists
class Node:
    def __init__(self,initData):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newData):
        self.data = newData

    def setNext(self,newNext):
        self.next = newNext

#Defining unordered linked lists
class UnorderedList:

    def __init__(self):
        self.head = None

    #printing unordered linked list in brackets without commas or apostrophes
    def __str__(self):
        current = self.head

        nodes = []

        while current != None:
            nodes.append(str(current.getData()))
            current = current.getNext()

        return ('[ %s ]' % ' '.join(map(str, nodes)))

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()

        return count

    #search that returns a boolean
    def search(self,item):
        found = False
        current = self.head

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    #search that returns the item if it exists, none if it doesn't exist
    def retrieve(self, item):     
        current = self.head

        while current != None:
            if current.getData().name == item:
                return current.getData()
            else:
                current = current.getNext()
        
        return None
    
    def remove(self,item):
        # and we're assuming item MUST be present

        found = False
        previous = None
        current = self.head

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # if I get to this point, "current" points to the
        # item I want to delete

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

#Defining user class, people with accounts
class User:
    def __init__(self, name):
        self.name = name
        #collecting each users' friends in a linked list
        self.friends = UnorderedList()

    def __str__(self):
        return self.name

#Function that adds a user object to accounts linked list
def addAnAccount(accounts, name):
    if accounts.retrieve(name) == None:
        user = User(name)
        accounts.add(user)
        print('   ', name, 'now has an account.')
        
    else:
        print('    A person with name', name, 'already exists.')

    print()

#Functions that adds a user to another user's friends linked list 
def addAFriend(accounts, user, friend):
    if user == friend:
        print('    A person cannot friend him/herself.')

    #checking to see if both users exist in the accounts list   
    elif accounts.retrieve(user) == None:
        print('    A person with name', user, 'does not currently exist.')
        
    elif accounts.retrieve(friend) == None:
        print('    A person with name', friend, 'does not currently exist.')

    #checking to see if the two users are already friends
    elif accounts.retrieve(user).friends.search(friend):
        print('   ', user, 'and', friend, 'are already friends.')
        
    else:
        accounts.retrieve(user).friends.add(friend)
        accounts.retrieve(friend).friends.add(user)
        print('   ', user, 'and', friend, 'are now friends.')
        
    print()

#Function to remove a user from another user's friends list
def deleteAFriend(accounts, user, friend):
    if user == friend:
        print('    A person cannot unfriend him/herself.')

    #checking to see if both users exist in the accounts list
    elif accounts.retrieve(user) == None:
        print('    A person with name', user, 'does not currently exist.')
        
    elif accounts.retrieve(friend) == None:
        print('    A person with name', friend, 'does not currently exist,')

    #checking to see if users are friends   
    elif not accounts.retrieve(user).friends.search(friend):
        print('   ', user, 'and', friend, \
              "aren't friends, so you can't unfriend them.")
        
    else:
        accounts.retrieve(user).friends.remove(friend)
        accounts.retrieve(friend).friends.remove(user)
        print('   ', user, 'and', friend, 'are no longer friends.')

    print()

#Function to list all the friends of a user
def listAllFriends(accounts, user):
    if accounts.retrieve(user).friends.isEmpty():
        print('   ', user, 'has no friends.')
        
    else:
        print('   ', accounts.retrieve(user).friends)

    print()

#Function that checks if the two users are friends or not
def queryFriendStatus(accounts, user, friend):
    if user == friend:
        print('    A person cannot query him/herself.')

    #checking to see if both users exist in accounts list
    elif accounts.retrieve(user) == None:
        print('    A person with name', user, 'does not currently exist.')
        
    elif accounts.retrieve(friend) == None:
        print('    A person with name', friend, 'does not currently exist.')
    
    elif accounts.retrieve(user).friends.search(friend):
        print('   ', user, 'and', friend, 'are friends.')
        
    else:
        print('   ', user, 'and', friend, 'are not friends.')

    print()
    
def main():
    #creating linked list to collect all users
    accounts = UnorderedList()

    file = open('FriendData.txt', 'r')

    for line in file:
        line = line.split()

        command = line[0]

        #printing each line in the text file
        print('-->', *line)

        #perform action according to command in text file
        if command == 'Person':
            addAnAccount(accounts, line[1])
            
        elif command == 'Friend':
            addAFriend(accounts, line[1], line[2])
            
        elif command == 'Unfriend':
            deleteAFriend(accounts, line[1], line[2])
            
        elif command == 'List':
            listAllFriends(accounts, line[1])
            
        elif command == 'Query':
            queryFriendStatus(accounts, line[1], line[2])
            
        elif command == 'Exit':
            print('    Exiting...')
            break

    file.close()

main()
    
