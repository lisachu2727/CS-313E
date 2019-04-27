#File: htmlChecker.py
#Description: HW 4
#Student's Name: Lisa Chu
#Student's UT EID: tc29328
#Course Name: CS 313E
#Unique Number: 50739
#
#Date Created: 3/4/2019
#Date Last Modified: 3/8/2019

class Stack(object):
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def getTag(textFile,tagList):
    string = ''

    file = open(textFile, 'r')
    character = file.read(1)
    appending = False
    readingFile = True

    while readingFile:    
        for character in file.read():
            
            #Signal to start appending
            if character == '<':
                appending = True
            elif appending == True:
                if character == '>' or character == ' ':
                    tagList.append(string)  #Appending tag to list
                    string = ''             #Resetting string
                    appending = False       #Signal to stop appending
                    
                #Unless character is '>' or ' ', append to string
                else:
                    string += character
        break
    
    file.close()
        
def main():
    #Initializing lists and stack
    tagList = []
    VALIDTAGS = []
    tagStack = Stack()

    #Tags that do not need matching start and end tags
    EXCEPTIONS = ['meta', 'br', 'hr']

    getTag('htmlfile.txt', tagList)

    #Iterate over list of tags obtained through getTag function
    for i in range(0, len(tagList) - 1):
        #If not an end tag
        if tagList[i][0] != '/':

            #If tag is not an exception, add to stack
            if (tagList[i] not in EXCEPTIONS):
                tagStack.push(tagList[i])
                print('Tag ', tagList[i],' pushed: stack is now \t\t\t', \
                      tagStack, sep = '')
                print()

                #If tag not already in VALIDTAGS, add to VALIDTAGS
                if tagList[i] not in VALIDTAGS:
                    VALIDTAGS.append(tagList[i])
                    print('New tag ', tagList[i], ' found and added to list' \
                          ' of valid tags', sep = '')
                    print()

            #Print out for exception tags
            else:
                print('Tag ', tagList[i], ' does not need to match: stack is' \
                      ' still \t', tagStack, sep = '')
                print()

        #If ending tag matches top of stack, pop from stack 
        elif tagList[i][1:len(tagList[i])] == tagStack.peek():
            tagStack.pop()
            print('Tag ', tagList[i], ' matches top of stack: ', \
                  'stack is now \t', tagStack, sep = '')
            print()

        #If there is still tags left in the list and they do not match
        #the top of the stack
        else:
            print('Error: tag is', tagList[i], 'but top of stack is', \
                  tagStack.peek())
            print()

    #Checking if stack containing tags are empty
    if tagStack.isEmpty():
        print('Processing complete. No mismatches found.')
        print()
    else:
        print('Processing complete. Unmatched tages remain on stack : \t',
              tagList)
        print()

    print('This is the list of all the tags found: ')
    print(tagList, '\n')
    
    print('Valid tags: ')
    print(VALIDTAGS, '\n')
    
    print('Exceptions: ')
    print(EXCEPTIONS)
           
main()
    
