import datetime

def checkItemExists(taskName):

    global ToDoList

    for task in ToDoList:
        if taskName == task[0]:
            return True
    return False


def takeSecond(element):

    return element[1]


def addNewItems(): #Adding a new item to the to do list 
    global ToDoList
    task = input('\nEnter the name of the task : ') 
    date_time  = input("Enter the task completion date (yyyy/mm/dd HH:MM:SS) : ")


    datetime_obj = datetime.datetime.strptime(date_time,'%Y/%m/%d %H:%M:%S')



    if datetime_obj<datetime.datetime.now():
        print('Time entered is in the past! Select the options again')
        return



    if checkItemExists(task):
        print('Task already exists! Select the options again')
        return



    ToDoList.append((task,datetime_obj))
    print('\nTask added successfully')


    ToDoList.sort(key = takeSecond)
    return


def printListItems():

    global ToDoList
    print('')
    for ind,task in enumerate(ToDoList):
        print(f"{ind}. {task[1]} - {task[0]}")
    return


def removeListItems():

    global ToDoList
    index_to_delete = int(input('Enter which task would you like to delete [select index wise starting from 0] : '))

    del ToDoList[index_to_delete]
    print('Task deleted successfully')



ToDoList = []


while True: #While true loop begins here

    print('\n1. Print below the list of all to do items') #Prints below the list of all to do items
    print('2. Enter a new to do item ')
    print('3. Remove a to do item')
    print('4. Quit')
    choice  = int(input('\nNow please enter a choice : ')) #Prompts the user to enter a choice of the list of options

    if choice == 1:
        printListItems()
    elif choice == 2:
        addNewItems()
    elif choice == 3:
        removeListItems()


    elif choice == 4:
        print('End of program') #Program ends here
 
        break
