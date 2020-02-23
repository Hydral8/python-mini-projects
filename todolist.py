todos = []


def addTodo():
    print("What item would you like to add!")
    item = input()
    if(item in todos):
        print("Item already exists!")
    else:
        todos.append(item)


def removeTodo():
    print("What item would you like to remove?")
    print(todos)
    item = input()
    try:
        todos.remove(item)
        print("Completed!")
    except:
        print("Item Does Not Exist!")


def printTodos():
    print(todos)


while(True):
    print("ADD, REMOVE, or GET todos?")
    userInput = input()
    if(userInput.upper() == "ADD"):
        addTodo()
    elif(userInput.upper() == "REMOVE"):
        removeTodo()
    elif(userInput.upper() == "GET"):
        printTodos()
    else:
        print("INVALID COMMAND")
