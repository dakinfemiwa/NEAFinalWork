# Module for a tree to generate binary tree search
class Tree:
    # Initialises values
    def __init__(self, data):
        # This stores all the nodes in their original order to
        #   make accessing adjacent nodes a bit easier
        self.__NodeCount = len(data)
        self.__ArrayData = []
        # Implementation of he tree itself
        self.__TreeTable = []
        # Adds each node to the first index of each dimension of the TreeTable array
        self.__AddArray(data)

    # Module to add each node to the first index of each dimension of the TreeTable array
    def __AddArray(self, data):
        for node in data:
            self.__TreeTable.append([node, None, None])
            self.__ArrayData.append(node)
        self.__PlaceNode(0, 1, data)
        #print(self.__TreeTable)

    # Places the nodes in their respective places for a binary tree
    #   Also sorts every value in a specific order
    def __PlaceNode(self, parentIndex, childIndex, Node):
        # If the child node is less than the parent node it is moved to the left of the tree while if the child node
        #   is greater than the parent node it is moved to the left of teh tree
        try:
            if Node[childIndex] < Node[parentIndex]:
                empty = self.__CheckIfEmpty("Left", parentIndex)
                if empty == True:
                    if (Node[childIndex] < self.__TreeTable[0][0]) and (Node[parentIndex] > self.__TreeTable[0][0]):
                        parentNode = self.__TreeTable[0][0]
                        parentIndex = self.__ArrayData.index(parentNode)
                        self.__PlaceNode(parentIndex, childIndex, Node)

                    self.__TreeTable[parentIndex][1] = Node[childIndex]
                    childIndex += 1
                    # Recursive algorithm for each new node
                    self.__PlaceNode(0, childIndex, Node)
                else:
                    parentIndex = Node.index(self.__TreeTable[parentIndex][1])
                    self.__PlaceNode(parentIndex, childIndex, Node)

            elif Node[childIndex] > Node[parentIndex]:


                empty = self.__CheckIfEmpty("Right", parentIndex)
                if empty == True:
                    if (Node[childIndex] > self.__TreeTable[0][0]) and (Node[parentIndex] < self.__TreeTable[0][0]):
                        parentNode = self.__TreeTable[0][0]
                        parentIndex = self.__ArrayData.index(parentNode)
                        self.__PlaceNode(parentIndex, childIndex, Node)

                    self.__TreeTable[parentIndex][2] = Node[childIndex]
                    childIndex += 1
                    self.__PlaceNode(0, childIndex, Node)
                else:

                    parentIndex = Node.index(self.__TreeTable[parentIndex][2])
                    self.__PlaceNode(parentIndex, childIndex, Node)
        except IndexError:
            return

    # Check if a tree is full on one side or not
    def __CheckIfEmpty(self, LoR, parentIndex):
        if LoR == "Left":
            index = 1
        elif LoR == "Right":
            index = 2

        if self.__TreeTable[parentIndex][index] == None:
            return True
        else:
            return False

    # Module that carries out the binary tree search
    def Search(self, item):
        # If the item is smaller than the parent node, the search goes to the left, while if it is greater
        #   than the parent node then it goes towards the right of the tree
        self.__Found = False
        self.__Searches = 0
        self.__Search(item, 0)


        # If the item was found the Boolean attribute will change in the private method Search
        return self.__Found

    def __Search(self, item, index):
        if self.__Searches <= self.__NodeCount:

            # Checks if the value is found and changes the Boolean attribute if so
            if self.__TreeTable[index][0] == item:
                self.__Found = True
                return

            # Checks if the item being looked for is greater than the current node
            empty = self.__CheckIfEmpty("Right", index)

            if empty == False:
                if item > self.__TreeTable[index][0]:
                    newSearchValue = self.__TreeTable[index][2]
                    #print(newSearchValue)
                    index = self.__ArrayData.index(newSearchValue)
                    self.__Searches +=1
                    self.__Search(item, index)

            # Checks if the item being looked for is smaller than the current node
            empty = self.__CheckIfEmpty("Left", index)
            #print(empty)
            if empty == False:
                if self.__TreeTable[index][0] > item:
                    newSearchValue = self.__TreeTable[index][1]
                    index = self.__ArrayData.index(newSearchValue)
                self.__Searches += 1
                self.__Search(item, index)


class BinaryTreeArray:
    # Initialises values
    def __init__(self, data, index):
        # This stores all the nodes in their original order to
        #   make accessing adjacent nodes a bit easier
        self.__NodeCount = len(data)
        self.__ArrayData = []
        # Implementation of he tree itself
        self.__TreeTable = []
        #Shows what index should be used to order the list
        self.__Index = index
        # Adds each node to the first index of each dimension of the TreeTable array
        self.__AddArray(data)

    # Module to add each node to the first index of each dimension of the TreeTable array
    def __AddArray(self, data):
        for node in data:
            self.__TreeTable.append([node, None, None])
            self.__ArrayData.append(node)
        self.__PlaceNode(0, 1, data)
        for node in self.__TreeTable:
            print(node)

    # Places the nodes in their respective places for a binary tree
    #   Also sorts every value in a specific order
    def __PlaceNode(self, parentIndex, childIndex, Node):

        # If the child node is less than the parent node it is moved to the left of the tree while if the child node
        #   is greater than the parent node it is moved to the left of teh tree
        try:
            parentNodeV = Node[parentIndex][self.__Index]
            childNodeV = Node[childIndex][self.__Index]

            print(parentNodeV, childNodeV)
            print(self.__TreeTable[0])

            if childNodeV < parentNodeV:
                empty = self.__CheckIfEmpty("Left", parentIndex)
                if empty == True:
                    if (childNodeV < self.__TreeTable[0][0][self.__Index]) and (parentNodeV > self.__TreeTable[0][0][self.__Index]):
                        parentNode = self.__TreeTable[0][0]
                        parentIndex = self.__ArrayData.index(parentNode)
                        self.__PlaceNode(parentIndex, childIndex, Node)

                    self.__TreeTable[parentIndex][1] = Node[childIndex]
                    childIndex += 1
                    # Recursive algorithm for each new node
                    self.__PlaceNode(0, childIndex, Node)
                else:
                    parentIndex = Node.index(self.__TreeTable[parentIndex][1])
                    self.__PlaceNode(parentIndex, childIndex, Node)

            elif childNodeV > parentNodeV:
                empty = self.__CheckIfEmpty("Right", parentIndex)
                if empty == True:
                    if (Node[childIndex][self.__Index] > self.__TreeTable[0][0][self.__Index]) and (Node[parentIndex][self.__Index] < self.__TreeTable[0][0][self.__Index]):
                        parentIndex = 0
                        self.__PlaceNode(parentIndex, childIndex, Node)
                    if empty == True:
                        print("PN", parentIndex)
                        print("SETTING IT TO RIGHT NODE")
                        self.__TreeTable[parentIndex][2] = Node[childIndex]
                        print("NEW")
                        print(self.__TreeTable[parentIndex][2])
                        childIndex += 1
                        self.__PlaceNode(0, childIndex, Node)
                else:
                    parentIndex = Node.index(self.__TreeTable[parentIndex][2])
                    self.__PlaceNode(parentIndex, childIndex, Node)
        except IndexError:
            return

    # Check if a tree is full on one side or not
    def __CheckIfEmpty(self, LoR, parentIndex):
        if LoR == "Left":
            index = 1
        elif LoR == "Right":
            index = 2

        if self.__TreeTable[parentIndex][index] == None:
            return True
        else:
            return False

    # Module that carries out the binary tree search
    def Search(self, item):
        # If the item is smaller than the parent node, the search goes to the left, while if it is greater
        #   than the parent node then it goes towards the right of the tree
        self.__Found = False
        self.__Searches = 0
        self.__Search(item, 0)

        # If the item was found the Boolean attribute will change in the private method Search
        return self.__Found

    def __Search(self, item, index):
        if self.__Searches <= self.__NodeCount:

            # Checks if the value is found and changes the Boolean attribute if so
            if self.__TreeTable[index][0] == item:
                self.__Found = True
                return

            # Checks if the item being looked for is greater than the current node
            empty = self.__CheckIfEmpty("Right", index)

            if empty == False:
                if item > self.__TreeTable[index][0]:
                    newSearchValue = self.__TreeTable[index][2]
                    # print(newSearchValue)
                    index = self.__ArrayData.index(newSearchValue)
                    self.__Searches += 1
                    self.__Search(item, index)

            # Checks if the item being looked for is smaller than the current node
            empty = self.__CheckIfEmpty("Left", index)
            # print(empty)
            if empty == False:
                if self.__TreeTable[index][0] > item:
                    newSearchValue = self.__TreeTable[index][1]
                    index = self.__ArrayData.index(newSearchValue)
                self.__Searches += 1
                self.__Search(item, index)

    def Traverse(self):
        self.__TraverseArray = []
        self.__InOrderTraverse(0)
        return self.__TraverseArray

    def __InOrderTraverse(self, index):
        if 1:
            print(self.__TraverseArray)
            empty = self.__CheckIfEmpty("Left", index)
            if empty == False:
                leftNode = self.__TreeTable[index][1]
                leftIndex = self.__ArrayData.index(leftNode)
                self.__InOrderTraverse(leftIndex)

            self.__TraverseArray.append(self.__TreeTable[index][0])

            empty = self.__CheckIfEmpty("Right", index)
            if empty == False:
                rightNode = self.__TreeTable[index][2]
                rightIndex = self.__ArrayData.index(rightNode)
                self.__InOrderTraverse(rightIndex)
        #except TclError:
        #   pass

values = [[1, 1093.0, 5, '114.4'],
          [2, 1092.5, 7, '115.6'],
          [3, 1093.0, 8, '117.4'],
          [4, 1106.0, 1, '42.9'],
          [5, 1092.0, 2, '112.6'],
          [6, 1092.5, 9, '117.5'],
          [7, 1092.0, 4, '114.0'],
          [8, 1092.0, 3, '113.9'],
          [9, 1093.0, 6, '115.3']]