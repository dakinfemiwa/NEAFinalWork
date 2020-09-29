import os, sys
orignialDir = os.getcwd()
"""try:
    os.chdir(os.getcwd() + "\\Tools")
except:
    pass
print(os.getcwd())"""
from Tools.Stack import Stack
os.chdir(orignialDir)

#Initialisesclass
class DirectoryHandler:
    def __init__(self):
        #Creates a stack with the directory at the Main file
        self.__directories = Stack([os.getcwd()])

    #Method to change directory to #/Images/Background
    def changeDirectoryToBackground(self):
        #Adds a new value to the stack
        self.__directories.Push(os.getcwd() + "\\Images\\Background")

        #Peeks for that directory
        self.__directory, Index = self.__directories.Peek()

        #Sets the directory to that value
        os.chdir(self.__directory)
        return True

    #Method to revert back the directory to the normal form
    def changeDirectoryToMain(self):
        #Pops the current directory from the stack
        self.__directories.Pop()

        #Peeks for the original directory
        self.__directory, Index = self.__directories.Peek()

        #Sets the dirctory to that directory
        os.chdir(self.__directory)
        return True


    #Method to change directory to /Main folder for database
    def changeDirectoryToMainFolder(self):
        #Pushes value to stack
        self.__directories.Push(os.getcwd() + "\\Main")

        #Peeks for the directory
        self.__directory, Index = self.__directories.Peek()

        #Sets the directory to the peek value
        os.chdir(self.__directory)
        return True

    #Method to change directory to /Images/Avatars
    def changeDirectoryToAvatar(self):
        #Pushes new directory into stack
        self.__directories.Push(os.getcwd() + "\\Images\\Avatars")

        #Peeks for the directory
        self.__directory, Index = self.__directories.Peek()

        #Changes directory to that value
        os.chdir(self.__directory)

        #Ends method
        return True

    #Method to change directory to /Images/Avatars2
    def changeDirectoryToAvatar2(self):
        #Pushes new directory into stack
        self.__directories.Push(os.getcwd() + "\\Images\\Avatars_Small")

        #Peeks for the directory
        self.__directory, Index = self.__directories.Peek()

        #Changes directory to that value
        os.chdir(self.__directory)

        #Ends method
        return True

    # Method to change directory to /Images/Dice
    def changeDirectoryToDice(self):
        # Pushes new directory into stack
        self.__directories.Push(os.getcwd() + "\\Images\\Dice")

        # Peeks for the directory
        self.__directory, Index = self.__directories.Peek()

        # Changes directory to that value
        os.chdir(self.__directory)

        #Ends method
        return True

    # Method to change directory to /Images/BackgroundGame
    def changeDirectoryToBackgroundGame(self):
        # Pushes new directory into stack
        self.__directories.Push(os.getcwd() + "\\Images\\BackgroundGame")

        # Peeks for the directory
        self.__directory, Index = self.__directories.Peek()

        # Changes directory to that value
        os.chdir(self.__directory)

        return True

    # Method to change directory to /Images/GameProps
    def changeDirectoryToGameProps(self):
        # Pushes new directory into stack
        self.__directories.Push(os.getcwd() + "\\Images\\GameProps")

        # Peeks for the directory
        self.__directory, Index = self.__directories.Peek()

        # Changes directory to that value
        os.chdir(self.__directory)

        #Ends method
        return True

    # Method to change directory to /Images/BackgroundGameNA
    def changeDirectoryToBackgroundGameNA(self):
        # Pushes new directory into stack
        self.__directories.Push(os.getcwd() + "\\Images\\BackgroundGameNA")

        # Peeks for the directory
        self.__directory, Index = self.__directories.Peek()

        # Changes directory to that value
        os.chdir(self.__directory)

        # Ends method
        return True

    # Method to change directory to /Images/BackgroundGameNF
    def changeDirectoryToBackgroundNF(self):
        # Pushes new directory into stack
        self.__directories.Push(os.getcwd() + "\\Images\\BackgroundNF")

        # Peeks for the directory
        self.__directory, Index = self.__directories.Peek()

        # Changes directory to that value
        os.chdir(self.__directory)

        # Ends method
        return True

    # Method to change directory to /Images/Button
    def changeDirectoryToButton(self):
        # Pushes new directory into stack
        self.__directories.Push(os.getcwd() + "\\Images\\Button")

        # Peeks for the directory
        self.__directory, Index = self.__directories.Peek()

        # Changes directory to that value
        os.chdir(self.__directory)

        # Ends method
        return True

    #Method to list every image in a directory so that it can be resized by the resizing app
    def findImages(self):
        #Returns array of list of all the file names in the current directory
        files = os.listdir()

        #Returns the list stored in the local variable files
        return files
