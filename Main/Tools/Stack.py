class Stack:
    def __init__(self, items=[]):
        self.__Items = items
        #Set at -1 so when first item is pushed onto empty stack it points at its
        #   array index
        a = self.__CheckIfEmpty()
        if a == True:
            self.__Pointer = -1
        else:
            self.__Pointer = len(items) - 1

    def Push(self, data):
        #Adds data to stack and increments the pointer
        self.__Items.append(data)
        self.__Pointer += 1

    def Pop(self):
        #Checks if stack is empty and if it isn't removes data item
        #   and decrements the pointer
        empty = self.__CheckIfEmpty()
        if empty == False:
            self.__Items.pop(len(self.__Items) - 1)
            self.__Pointer -= 1
        else:
            #If stack is empty it sends an error message
            KeyError("Error: No items to pop from stack as stack is empty")

    def Peek(self):
        #Looks at the item on the stack. Checks if stack is empty to avoid errors
        empty = self.__CheckIfEmpty()
        if empty == False:
            return self.__Items[self.__Pointer],  self.__Pointer
        else:
            KeyError("Error: No items to peek as stack is empty")

    def __ResetPointer(self):
        self.__Pointer = len(self.__Items) - 1


    def __CheckIfEmpty(self):
        #Counts how many items are in the array and if it is equal to zero
        #   returns True otherwise returns False
        if len(self.__Items) > 0:
            return False
        else:
            return True

    def Print(self):
        print(self.__Items)
