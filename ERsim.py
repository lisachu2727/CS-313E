#File: ERsim.py
#Description: HW 5
#Student's Name: Lisa Chu
#Student's UT EID: tc29328
#Course Name: CS 313E
#Unique Number: 50739
#
#Date Created: 3/15/2019
#Date Last Modified: 3/15/2019

class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)
    
    def enqueue(self,item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)    
    
def addAPatient(patient, condition, critical, serious, fair):
    if condition == 'Critical':
        critical.enqueue(patient)
    elif condition == 'Serious':
        serious.enqueue(patient)
    elif condition == 'Fair':
        fair.enqueue(patient)

    print('--> Add', patient, 'to', condition, 'queue')
    printAllQueues(critical, serious, fair)


def treatPatient(treatAction, critical, serious, fair):
    if treatAction == 'next':
        print('--> Treat next patient')
        print()
        
        if not critical.isEmpty():
            patient = critical.dequeue()
            print('Treating', patient, 'from Critical queue')
            printAllQueues(critical, serious, fair)

        elif not serious.isEmpty():
            patient = serious.dequeue()
            print('Treating', patient, 'from Serious queue')
            printAllQueues(critical, serious, fair)

        elif not fair.isEmpty():
            patient = fair.dequeue()
            print('Treating', patient, 'from Fair queue')
            printAllQueues(critical, serious, fair)
        else:
            print('No patients in queues')
            print()

    elif treatAction == 'Critical' or treatAction == 'Serious' or \
         treatAction == 'Fair':
        print('--> Treat next patient on', treatAction, 'queue')
        print()

        if treatAction == 'Critical' and not critical.isEmpty():
            patient = critical.dequeue()
            print('Treating', patient, 'from Critical queue')
            printAllQueues(critical, serious, fair)

        elif treatAction == 'Serious' and not critical.isEmpty():
            patient = serious.dequeue()
            print('Treating', patient, 'from Serious queue')
            printAllQueues(critical, serious, fair)

        elif treatAction == 'Fair' and not critical.isEmpty():
            patient = fair.dequeue()
            print('Treating', patient, 'from Fair queue')
            printAllQueues(critical, serious, fair)

        else:
            print('No patients in queues')
            print()

    elif treatAction == 'all':
        print('--> Treat all patients')
        print()

        while not critical.isEmpty():
            patient = critical.dequeue()
            print('Treating', patient, 'from Critical queue')
            printAllQueues(critical, serious, fair)

        while not serious.isEmpty():
            patient = serious.dequeue()
            print('Treating', patient, 'from Serious queue')
            printAllQueues(critical, serious, fair)

        while not fair.isEmpty():
            patient = fair.dequeue()
            print('Treating', patient, 'from Fair queue')
            printAllQueues(critical, serious, fair)

        print('No patients in queues')
        print()
            
def printAllQueues(critical, serious, fair):
    print()
    print('Queues are:')
    print('Fair: \t\t', fair)
    print('Serious: \t', serious)
    print('Critical: \t', critical)
    print()
    
def main():
    critical = Queue()
    serious = Queue()
    fair = Queue()

    file = open('ERsim.txt', 'r')

    for line in file:
        line = line.split()

        command = line[0]
        
        if command == 'add':
            addAPatient(line[1], line[2], critical, serious, fair)
        elif command == 'treat':
            treatPatient(line[1], critical, serious, fair)
        elif command == 'exit':
            print('--> Exit')

    file.close()
            
main()
    
