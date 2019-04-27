#File: LinkedLists.py
#Description: HW 6
#Student's Name: Lisa Chu
#Student's UT EID: tc29328
#Course Name: CS 313E
#Unique Number: 50739
#
#Date Created: 3/29/2019
#Date Last Modified: 3/29/2019

#defining Node class
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

#defining LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head

        #collecting nodes in a linked list to print out
        
        nodes = []

        while current != None:
            nodes.append(current.getData())
            current = current.getNext()

        #printing in rows of 10 with 2 spaces between each node
            
        i = 0
        for node in nodes:
            print(str(node), end = '  ')
            i += 1
            if i % 10 == 0:
                print('\n', end = '')
        return ''

    #add to the beginning of the linked list
    def addFirst(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    #add to the end of the linked list
    def addLast(self, item):
        temp = Node(item)

        current = self.head
        previous = None

        while current != None:
            previous = current
            current = current.getNext()

        if previous == None:
            self.head = temp
        else:
            previous.setNext(temp)

    #add item in order to linked list
    def addInOrder(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        temp.setNext(current)

        #testing if node is the first item of the linked list
        
        if previous == None:
            self.head = temp
        else:
            previous.setNext(temp)

    #getting number of nodes in linked list
    def getLength(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()

        return count

    #searching for an item in an unordered linked list
    def findUnordered(self, item):
        found = False
        current = self.head

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    #searching for an item in an ordered linked list
    def findOrdered(self, item):
        found = False
        stop = False
        current = self.head

        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                #stop searching if next item is greater than current item
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    #removing item that may or may not be in linked list
    def delete(self, item):
        found = False
        previous = None
        current = self.head

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
                
        #removing item if found in linked list
        if found:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

        return found

    #copying a linked list while keeping original intact
    def copyList(self):
        copiedList = LinkedList()
        current = self.head
        
        nodes = []
        
        #storing original nodes in a list
        while current != None:
            nodes.append(current.getData())
            current = current.getNext()

        #creating new linked list in same order as original list
        for i in range(len(nodes)):
            copiedList.addLast(nodes[i])

        return copiedList

    #copying a linked list in reverse order while keeping original intact
    def reverseList(self):
        reversedList = LinkedList()
        current = self.head
        nodes = []

        #storing original nodes in a list
        while current != None:
            nodes.append(current.getData())
            current = current.getNext()

        #creating a new linked list in reverse order
        for i in range(len(nodes)):
            reversedList.addFirst(nodes[i])

        return reversedList

    #ordering a copy of a linked list while keeping original intact
    def orderList(self):
        orderedList = LinkedList()
        current = self.head
        nodes = []

        #storing original nodes in a list
        while current != None:
            nodes.append(current.getData())
            current = current.getNext()

        #creating a new linked list in order
        for i in range(len(nodes)):
            orderedList.addInOrder(nodes[i])

        return orderedList

    #testing if linked list is ordered
    def isOrdered(self):
        current = self.head
        previous = current
        
        stop = False
        ordered = True

        while current != None and not stop:
            #not ordered if previous data is greater than current data
            if previous.getData() > current.getData():
                stop = True
                ordered = False
            else:
                previous = current
                current = current.getNext()

        return ordered

    #testing if linked list is empty
    def isEmpty(self):
        return self.head == None

    #combine 2 ordered linked lists into 1 ordered linked list while
    #keeping originals intact
    def mergeList(self, b):
        mergedList = self.copyList()

        current = b.head

        while current != None:
            mergedList.addInOrder(current.getData())
            current = current.getNext()

        return mergedList

    #testing if 2 linked lists are equal
    def isEqual(self, b):
        equal = True

        current = self.head
        currentB = b.head

        #testing nodes one by one
        while current != None and currentB != None:
            if current.getData() != currentB.getData():
                equal = False
            else:
                current = current.getNext()
                currentB = currentB.getNext()

        #testing length of linked lists
        if self.getLength() != b.getLength():
            equal = False

        return equal

    #copying a linked list to not contain duplicates while keeping
    #original intact
    def removeDuplicates(self):
        noDuplicatesList = self.copyList()
        nodes = []

        current = noDuplicatesList.head
        previous = None

        while current != None:
            node = current.getData()
            #storing nodes in a list
            if node not in nodes:
                nodes.append(node)
                previous = current
                current = current.getNext()
            else:
                #testing if duplicate is at the beginning of the linked list
                #removing duplicate if node is already in list
                if previous == None:
                    noDuplicatesList.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                    current = previous.getNext()

        return noDuplicatesList
                          
def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of orderList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto?")
   
   print ("   Original list:")
   print (planets)
   print ("   Ordered list:")
   orderedPlanets = planets.orderList()
   print (orderedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isOrdered:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Ordered? ", planets.isOrdered())
   orderedPlanets = planets.orderList()
   print ("   After ordering:")
   print (orderedPlanets)
   print ("   ordered? ", orderedPlanets.isOrdered())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()
        
