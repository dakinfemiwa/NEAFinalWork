import tkinter
import threading
from DirectoryHandler import DirectoryHandler
from sizingAdjust import sizingAdjust
from tkinter import *
from tkinter import ttk
from Tools.User import User
from Tools.DataHandler import DataHandler
from Tools.Stack import Stack
from Tools.Theme import Theme
from Tools.Tree import Tree
from Menu import Main
import os,sys
import time

#Initialising parent slide class
class Slide:
    def __init__(self, window, sizeAdjust, imageURL, text, avatar):

        self.__Theme = Theme()
        self.InterfaceTheme = self.__Theme.getTheme()
        #Assign a window to that slide
        self.SlideFrame = Canvas(window, bg=self.__Theme.getBackground1(), bd=0)

        self.done = False
        self.text = text
        self.avatar = avatar


        #Links window to slide and gathers useful variables
        self.window = window
        self.Fonts = [90, 80, 70, 60, 50, 40, 30, 20]
        self.FontFamily = ["Microsoft YaHei UI Light", "Ebrima"]
        self.interfaceDirectory = os.getcwd()
        self.padding = 80

        #Gets data for correct sizings
        self.sizings = sizeAdjust#sizingAdjust(self.window, self.FontFamily, self.Fonts, self.padding, self.interfaceDirectory)

        #Initialises object that will handle shifts in directories
        self.DirectoryHandler = DirectoryHandler()

        print(self.sizings.FontFamily)

        if "\\Images\\Background" in self.interfaceDirectory:
            self.interfaceDirectory = os.getcwd()[0: len(os.getcwd()) - len('\\Images\\Background')]
            os.chdir(self.interfaceDirectory)
        elif "\\Main" in self.interfaceDirectory:
            self.interfaceDirectory = os.getcwd()[0: len(os.getcwd()) - len('\\Main')]
        os.chdir(self.interfaceDirectory)

        #Changes the directory to the images section where it can use the images to create a widget
        #   which will display the background
        self.DirectoryHandler.changeDirectoryToBackground()
        BGPhotoImage = PhotoImage(file=imageURL)
        self.backgroundLabel = Label(self.SlideFrame, image=BGPhotoImage, borderwidth=0, highlightthickness=0)
        self.backgroundLabel.image = BGPhotoImage
        self.backgroundLabel.place(relx=.0, rely=.0, width=self.sizings.width, height=self.sizings.height)
        #Redirects the directory back to the normal directory needed for the program


    def viewSlide(self):
        #Displays slide to be visible to the user
        self.SlideFrame.place(relx=self.sizings.canvasPosX, rely=self.sizings.canvasPosY, width=self.sizings.width, height=self.sizings.height)

    def closeSlide(self):
        #Gets rid of the current slide in way for another slide
        self.SlideFrame.place_forget()

class Welcome(Slide):
    def __init__(self, window, sizeAdjust, imageURL, text="", avatar=""):
        #Inherits the methods and attribbutes of the parent slide
        super(Welcome, self).__init__(window, sizeAdjust, imageURL, text, avatar)
        self.__Theme = Theme()
        #Gathers neccessary attributes for implementation
        self.imageURL = imageURL

        self.__ImplementSlides()

    def viewSlide(self):
        #Displays slide to be visible to the user
        self.SlideFrame.place(relx=self.sizings.canvasPosX, rely=self.sizings.canvasPosY, width=self.sizings.width, height=self.sizings.height)


    def __ImplementSlides(self):
        #A module that covers how the type of 'slide' is supposed to look
        proceedText = "Press any key to continue"

        self.backgroundLabel.destroy()
        del self.backgroundLabel

        BgPhotoImage = PhotoImage(master=self.SlideFrame, file=self.imageURL)

        self.backgroundLabel = Label(self.SlideFrame, image=BgPhotoImage, borderwidth=0, highlightthickness=0)
        self.backgroundLabel.place(relx=0, rely=0)
        self.backgroundLabel.image = BgPhotoImage

        #Motivational quote to encoruage end user
        quote = "An investment in knowledge pays the best interest."

        #Resets directory to original directory
        self.DirectoryHandler.changeDirectoryToMain()

        #Creates frame where the welcome message and proceed message will be
        self.InterfaceCanvas = Frame(self.SlideFrame, bg=self.__Theme.getBackground1(), bd=0)
        self.InterfaceCanvas.place(relx=0, rely=.05, height=0.9 * self.sizings.height, width=.65* self.sizings.width)

        #Displays welcome message
        self.WelcomeMessage = Label(self.SlideFrame, text="Welcome ",
                                    font=(self.sizings.FontFamily[0], self.sizings.FontSize[4]),
                                    anchor=W, bg=self.__Theme.getBackground1(),
                                    fg=self.__Theme.getForeground1())
        self.WelcomeMessage.place(relx=.05, rely=.1, width=.6 * self.sizings.width)

        #Displays motivational quote
        self.Quote = Message(self.SlideFrame, text=quote, font=(self.sizings.FontFamily[0], self.sizings.FontSize[7], "italic"),
                             anchor=W, bg=self.__Theme.getBackground1(), width=600*(self.sizings.width/1366),
                             fg=self.__Theme.getForeground1())
        self.Quote.place(relx=.05, rely=.25, width=.6 * self.sizings.width)

        #Displays Proceed Arrows
        self.ProcceedArrows = Label(self.InterfaceCanvas, text=">>",
                                    font=(self.sizings.FontFamily[0], self.sizings.FontSize[4] * 2),
                                    bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1())
        self.ProcceedArrows.place(relx=.7, rely=.55)

        #Displays text telling user to press a key to continue
        self.ProcceedText = Label(self.InterfaceCanvas, text=proceedText,
                                  font=(self.sizings.FontFamily[0], self.sizings.FontSize[7], "italic"),
                                  bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1())
        self.ProcceedText.place(relx=.55, rely=.8)

class Narration(Slide):
    def __init__(self, window, sizeAdjust, imageURL, text, pos, avatar=""):
        #Inherits methods and attributes from parent class
        super().__init__(window, sizeAdjust, imageURL, text, avatar)

        self.SlideFrame = self.SlideFrame

        self.__Theme = Theme()
        self.pos = pos
        self.imageURL = imageURL

        os.chdir(self.interfaceDirectory)
        self.DirectoryHandler = DirectoryHandler()

        #Creates a frame to use
        self.__SlideFrame = self.SlideFrame

        #Creates background, widgets, text and etc
        self.__ImplementSlides(self.pos)

    def viewSlide(self):
        #Displays slide to be visible to the user
        self.SlideFrame.place(relx=self.sizings.canvasPosX, rely=self.sizings.canvasPosY, width=self.sizings.width, height=self.sizings.height)


    def __ImplementSlides(self, textPos):
        #Changed directory to the main one
        try:
            pass
            self.DirectoryHandler.changeDirectoryToMain()
        except:
            print(os.getcwd())

        self.DirectoryHandler = DirectoryHandler()

        if textPos[0] == "T":
                if textPos == "TL":
                    xPos = 0
                    yPos = 0
                elif textPos == "TC":
                    xPos = 0.3
                    yPos = 0
                elif textPos == "TR":
                    xPos = 0.6
                    yPos = 0
        elif textPos[0] == "B":
                if textPos == "BL":
                    xPos = 0
                    yPos = 0.625
                elif textPos == "BC":
                    xPos = 0.3
                    yPos = 0.625
                elif textPos == "BR":
                    xPos = 0.6
                    yPos = 0.625

        self.DirectoryHandler.changeDirectoryToBackground()
        newPhotoImage = PhotoImage(file=self.imageURL)
        self.DirectoryHandler.changeDirectoryToMain()
        self.backgroundLabel.config(image=newPhotoImage)
        self.backgroundLabel.image = newPhotoImage

        self.widgetAvatarText = Message(self.__SlideFrame, bg=self.__Theme.getBackground1(), text=self.text,
                                        fg=self.__Theme.getForeground1(),
                                        width = int(round( 350 * (1366 / self.sizings.width) )),
                                        font=(self.sizings.FontFamily[0], self.sizings.FontSize[7]))
        self.widgetAvatarText.place(relx=xPos, rely=yPos, width=.4 * self.sizings.width,
                                    height=.375 * self.sizings.height)

    def closeSlide(self):
        #Gets rid of the current slide in way for another slide
        self.SlideFrame.place_forget()


class Convo(Slide):
    def __init__(self, window, sizeAdjust, imageURL, text, avatar):
        #Inherits methods and attributes from parent class
        super().__init__(window, sizeAdjust, imageURL, text, avatar)

        self.__Theme = Theme()
        self.imageURL = imageURL

        #Creates a frame to use
        self.__SlideFrame = self.SlideFrame
        #Creates background, widgets, text and etc
        self.__ImplementSlides()


    def viewSlide(self):
        #Displays slide to be visible to the user
        self.SlideFrame.place(relx=self.sizings.canvasPosX, rely=self.sizings.canvasPosY, width=self.sizings.width, height=self.sizings.height)

        self.SlideFrame.update()

    def __ImplementSlides(self):

        #Changed directory to the main one
        try:
            self.DirectoryHandler.changeDirectoryToMain()
        except:
            print(os.getcwd())

        self.DirectoryHandler = DirectoryHandler()
        #Changed directory to avatar section
        self.DirectoryHandler.changeDirectoryToAvatar()
        #Sets PhotoImage to avatar image
        avatarPhoto = PhotoImage(file=f'{self.avatar}.png')

        #Returns directory to main
        self.DirectoryHandler.changeDirectoryToMain()

        #Creates widget to display avatar
        widgetAvatar = Label(self.__SlideFrame, bg=self.__Theme.getBackground1(), bd=0, image=avatarPhoto)
        #Displays widget
        widgetAvatar.place(relx=.15, rely=.6, width=.2 * self.sizings.width, height=.4 * self.sizings.height)
        #Ensures image appears on widget
        widgetAvatar.image = avatarPhoto

        #Displays neccessary text
        self.widgetAvatarText = Message(self.__SlideFrame, bg=self.__Theme.getBackground1(), text= self.text, fg=self.__Theme.getForeground1(),
                                        font=(self.sizings.FontFamily[0], self.sizings.FontSize[7]))
        #Displays widget that displays neccessary text
        self.widgetAvatarText.place(relx=.35, rely=.6, width=.5 * self.sizings.width, height=.4 * self.sizings.height)

    def closeSlide(self):
        #Closes down slide
        self.SlideFrame.place_forget()
        self.SlideFrame.update()

    def ChangeSlide(self, text, bg=None):
        #Changes slide
        self.text = text
        self.widgetAvatarText['text'] = self.text

        if bg != None:
            self.imageURL = bg

            if "\\Main" in os.getcwd():
                os.chdir(self.interfaceDirectory)

            self.DirectoryHandler.changeDirectoryToBackground()

            bgPhotoImage = PhotoImage(file=self.imageURL)

            self.DirectoryHandler.changeDirectoryToMain()

            self.backgroundLabel.config(image=bgPhotoImage)
            self.backgroundLabel.image = bgPhotoImage


class Lesson(Slide):
    def __init__(self, window, sizeAdjust, imageURL, text, avatar, type):
        self.__Theme = Theme()
        super().__init__(window, sizeAdjust, imageURL, text, avatar)
        self.avatar = avatar
        self.text = text
        self.type = type
        self.Type = "Lessons"

    def viewSlide(self):
        self.__ImplementSlides()
        self.SlideFrame.place(relx=0, rely=0, width=self.sizings.width, height=self.sizings.height)

    def __ImplementSlides(self):
        text = self.avatar.upper() + "\n" + self.text

        self.DirectoryHandler.changeDirectoryToAvatar()

        AvatarPhotoImage = PhotoImage(file=self.avatar + '.png')

        #self.AvatarImage = PhotoImage
        AvatarFrame = Frame(self.SlideFrame, bg=self.__Theme.getBackground1())
        AvatarFrame.place(relx=.65, rely=.05, height=.45 * self.sizings.height, width=.45 * self.sizings.height)

        AvatarLabel = Label(AvatarFrame, image=AvatarPhotoImage)
        AvatarLabel.place(relx=0, rely=0)
        AvatarLabel.image = AvatarPhotoImage

        self.DirectoryHandler.changeDirectoryToMain()

        AvatarText = Message(self.SlideFrame, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(),
                                  font=(self.sizings.FontFamily[0], self.sizings.FontSize[7]), text=text)
        AvatarText.place(relx=.65, rely=.5, height=.45 * self.sizings.height, width=.45 * self.sizings.height)

        self.DiagramCanvas = Frame(self.SlideFrame, bg=self.__Theme.getBackground1(), bd=0)
        self.DiagramCanvas.place(relx=.05, rely=.05, width=.55 * self.sizings.width, height= .9 * self.sizings.height)

        self.DirectoryHandler.changeDirectoryToLessons()
        print(os.getcwd())

        if "Geometry" in self.type:
            FormulaMessage = Message(self.DiagramCanvas, bg="#F2F2F2", fg=self.__Theme.getForeground1(), font=(self.sizings.FontFamily[1], self.sizings.FontSize[7]) )
            FormulaMessage.place(relx=.0, rely=.9, width=.55* self.sizings.width, height=.1 * .9 * self.sizings.height)

            if self.type == "GeometryCircleArea":
                DiagramPhotoImage = PhotoImage(file="GeometryCirlceRadius.png")
                forumula = "\u03C0r\u00b2"
            elif self.type == "GeometryCirclePerimeter":
                DiagramPhotoImage = PhotoImage(file="GeometryCircleDiameter.png")
                forumula = "\u03C0d"
            elif self.type == "GeometrySquare":
                DiagramPhotoImage = PhotoImage(file="GeometrySquare.png")
                forumula = "l\u00b2"
            elif self.type == "GeometryRectangle":
                DiagramPhotoImage = PhotoImage(file="GeometryRectangle.png")
                forumula = "lw"
            elif self.type == "GeometryCylinder":
                DiagramPhotoImage = PhotoImage(file="GeometryCylinder.png")
                forumula = "\u03C0r\u00b2h"
            elif self.type == "GeometryCuboid":
                DiagramPhotoImage = PhotoImage(file="GeometryCuboid.png")
                forumula = "lwh"

            DiagramImage = Label(self.DiagramCanvas, image=DiagramPhotoImage, bg=self.__Theme.getBackground1())
            DiagramImage.place(relx=.125, rely=.025)
            DiagramImage.image = DiagramPhotoImage

            FormulaMessage['text'] = forumula

        if self.type[0:9] == "Coordinate":
            if self.type == "CoordinateLinearYIntercept":
                DiagramPhotoImage = PhotoImage(file="CoordinateLinearGradient.png")
            elif self.type == "CoordinateLinearBoat":
                DiagramPhotoImage = PhotoImage(file="CoordinateLinearBoat.png")
            elif self.type == "CoordinateQuadratic":
                DiagramPhotoImage = PhotoImage(file="CoordinateQuadratic.png")

            self.DirectoryHandler.changeDirectoryToMain()


class LoginPage(Slide):
    def __init__(self, window, sizeAdjust, imageURL, text="", avatar=""):
        #Inheritance where the parent class inherits methods and attributes from the child class
        super().__init__(window, sizeAdjust, imageURL, text, avatar)
        self.__Theme = Theme()
        self.Type = "Login"

        #Changes directory to original directory
        self.interfaceDirectory = os.getcwd()[0: len(os.getcwd()) - len('\\Images\\Background')]
        os.chdir(self.interfaceDirectory)

    def viewSlide(self):
        '''Method called to implement the slide'''
        self.__ImplementSlide()
        self.__SlideFrame = self.SlideFrame
        self.__SlideFrame.place(relx=0, rely=0, width=self.sizings.width, height=self.sizings.height)


    def __ImplementSlide(self):
        '''Displays the login'''
        self.DirectoryHandler.changeDirectoryToBackgroundGameNA()
        img = PhotoImage(file="SSofGame.png")
        self.DirectoryHandler.changeDirectoryToMain()

        #Frame displaying screenshot of game
        ScreenShotOfGameFrame = Frame(self.SlideFrame, bg=self.__Theme.getBackground1())
        ScreenShotOfGameFrame.place(relx=.075, rely=.125, width=0.3*self.sizings.width, height=0.75*self.sizings.height)

        #Image displaying screenshot of the image
        ScreenShotOfGameImage = Label(ScreenShotOfGameFrame, image=img)
        ScreenShotOfGameImage.image = img
        ScreenShotOfGameImage.place(relx=0, rely=0)

        #This frame stores the labels and entries for the login
        self.LoginFrame = Frame(self.SlideFrame, bg=self.__Theme.getBackground1())
        self.LoginFrame.place(relx=.45, rely=.125, width=.5*self.sizings.width, height=.75*self.sizings.height)

        #Displays the register tiele
        RegisterTitle = Label(self.LoginFrame, text="Login ",
                              font=(self.sizings.FontFamily[0], self.sizings.FontSize[5],"underline"),
                                    fg=self.__Theme.getForeground1(),
                                   anchor=W, bg=self.__Theme.getBackground1())
        RegisterTitle.place(relx=.05, rely=.05, width=.5 * self.sizings.width)

        #Displays Username and entry
        UsernameLabel = Label(self.LoginFrame, text="Username: ", font=(self.sizings.FontFamily[0], self.sizings.FontSize[7]),
                              anchor=W, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1())
        UsernameLabel.place(relx=.05, rely=.3)

        UsernameEntry = Entry(self.LoginFrame, font=(self.sizings.FontFamily[1], self.sizings.FontSize[7]),
                              relief="solid", fg=self.__Theme.getForeground1(), bg=self.__Theme.getBackground1())
        UsernameEntry.place(relx=.3, rely=.3, width=self.sizings.width * .3)

        #Displays Password and ENtry
        PasswordLabel = Label(self.LoginFrame, text="Password: ",
                              font=(self.sizings.FontFamily[0], self.sizings.FontSize[7]),
                              anchor=W, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1())
        PasswordLabel.place(relx=.05, rely=.5)

        PasswordEntry = Entry(self.LoginFrame, font=(self.sizings.FontFamily[1], self.sizings.FontSize[7]),
                              relief="solid", show="⚫", fg=self.__Theme.getForeground1(), bg=self.__Theme.getBackground1() )
        PasswordEntry.place(relx=.3, rely=.5, width=self.sizings.width * .3)

        #user presses this to submit data
        SubmitButton = Button(self.LoginFrame, text="Submit",
                              font=(self.sizings.FontFamily[0], self.sizings.FontSize[7], "underline"), relief="solid",
                              anchor=W, fg=self.__Theme.getForeground1(), bg=self.__Theme.getBackground1(), bd=1,
                              cursor="hand2", activebackground=self.__Theme.getBackground1(), padx=5, pady=5)
        SubmitButton.place(relx=.05, rely=.65)

        #User presses this to sign up
        SignUpButton = Button(self.LoginFrame, text="Sign Up",
                              font=(self.sizings.FontFamily[0], self.sizings.FontSize[7], "underline"), relief="solid",
                                   anchor=W, fg=self.__Theme.getForeground1(), bg=self.__Theme.getBackground1(), bd=1, command=lambda : self.__SignUp(), cursor="hand2",
                                   activebackground=self.__Theme.getBackground1(), padx=5, pady=5)
        SignUpButton.place(relx=.25, rely=.65)

        if "\\Images\\Background" in self.interfaceDirectory:
            self.interfaceDirectory = os.getcwd()[0: len(os.getcwd()) - len('\\Images\\Background')]
        os.chdir(self.interfaceDirectory)

        self.window.bind("<Key>", lambda event: self.__BlankMethod(event))
        SubmitButton.bind("<Button-1>",
                         lambda event: self.__CheckSignInDetails(event, (UsernameEntry.get(), PasswordEntry.get())))
        self.window.bind("<Return>", lambda event: self.__CheckSignInDetails(event, (UsernameEntry.get(), PasswordEntry.get())))
        #self.window.mainloop()

        widgetsTBChanged = [UsernameEntry, PasswordEntry, SubmitButton, SignUpButton]

        if self.InterfaceTheme == "dark":
            for widget in widgetsTBChanged:
                widget.config(highlightthickness=1, highlightcolor=self.__Theme.getForeground1(),
                              highlightbackground=self.__Theme.getForeground1(), borderwidth=3, bd=3)
            

        

    def __BlankMethod(self, event):
        pass

    def __SignUp(self):
        #Gets rid of old frame for login and sets up a new one
        self.LoginFrame.place_forget()

        #Replaces login frame and gets user to enter in a chosen username, password and gender
        self.LoginFrame = Frame(self.SlideFrame, bg=self.__Theme.getBackground1())
        self.LoginFrame.place(relx=.45, rely=.125, width=.5*self.sizings.width, height=.75*self.sizings.height)

        #Displays widgets
        RegisterTitle = Label(self.LoginFrame, text="Sign up ",
                              font=(self.sizings.FontFamily[0], self.sizings.FontSize[5], "underline"),
                              anchor=W, bg=self.__Theme.getBackground1(), )
        RegisterTitle.place(relx=.05, rely=.05, width=.5 * self.sizings.width)
        
        UsernameLabel = Label(self.LoginFrame, text="Username: ",
                                   font=(self.sizings.FontFamily[0], int(round(self.sizings.FontSize[7] * 0.7))),
                              anchor=W, fg=self.__Theme.getForeground1(), bg=self.__Theme.getBackground1())
        UsernameLabel.place(relx=.05, rely=.32)
        
        UsernameEntry = Entry(self.LoginFrame, font=(self.sizings.FontFamily[1], self.sizings.FontSize[7]), relief="solid",
                              fg=self.__Theme.getForeground1(), bg=self.__Theme.getBackground1())
        UsernameEntry.place(relx=.3, rely=.3, width=self.sizings.width * .3)
        
        PasswordLabel = Label(self.LoginFrame, text="Password: ",
                                   font=(self.sizings.FontFamily[0], int(round(self.sizings.FontSize[7] * 0.7))),
                              anchor=W, fg=self.__Theme.getForeground1(), bg=self.__Theme.getBackground1())
        PasswordLabel.place(relx=.05, rely=.42)
        
        PasswordEntry = Entry(self.LoginFrame, font=(self.sizings.FontFamily[1], self.sizings.FontSize[7]),
                              relief="solid", show="⚫", fg=self.__Theme.getForeground1(), bg=self.__Theme.getBackground1())
        PasswordEntry.place(relx=.3, rely=.4, width=self.sizings.width * .3)
        
        ConfirmPasswordLabel = Label(self.LoginFrame, text="Confirm Password: ",
                                          font=(self.sizings.FontFamily[0], int(round(self.sizings.FontSize[7] * 0.7))),
                                     anchor=W, fg=self.__Theme.getForeground1(), bg=self.__Theme.getBackground1())
        ConfirmPasswordLabel.place(relx=.05, rely=.52)
        
        ConfirmPasswordEntry = Entry(self.LoginFrame, font=(self.sizings.FontFamily[1], self.sizings.FontSize[7]), relief="solid",
                                     show="⚫", fg=self.__Theme.getForeground1(), bg=self.__Theme.getBackground1())
        ConfirmPasswordEntry.place(relx=.3, rely=.5, width=self.sizings.width * .3)


        #Button which when clicked validates the login details
        SignUpButton = Button(self.LoginFrame, text="Sign Up", font=(self.sizings.FontFamily[0], self.sizings.FontSize[7], "underline"),
                              relief="solid", anchor=W, bg=self.__Theme.getBackground1(), bd=1,
                              fg=self.__Theme.getForeground1(),
                              cursor="hand2", activebackground=self.__Theme.getBackground1(), padx=5, pady=5)
        SignUpButton.place(relx=.05, rely=.7)

        SignUpButton.bind("<Button-1>", lambda event:self.__CheckSignUpDetails(event, UsernameEntry.get(), PasswordEntry.get(),
                                                                        ConfirmPasswordEntry.get()))
        self.window.bind("<Return>", lambda event:self.__CheckSignUpDetails(event, UsernameEntry.get(), PasswordEntry.get(),
                                                                        ConfirmPasswordEntry.get()))
        self.window.mainloop()

        widgetsTBChanged = [UsernameEntry, PasswordEntry, ConfirmPasswordEntry, SignUpButton]

        if self.InterfaceTheme == "dark":
            for widget in widgetsTBChanged:
                widget.config(bg=self.__Theme.getBackground3(), fg=self.__Theme.getForeground1())


    def __GenerateUsernameKey(self, username):
        '''Hashing algorithm generated on username to generate index
        Converts each digit to its decimal ASCII value and then
           adds that value to the key, subtracts the ASCII value of the
           next digit and then multiplies it by the next and then adds it
           and so on'''

        key = 0
        for char in username:
            index = username.index(char)
            OpIndex = index % 3
            operators = ['+', '-', '*']
            ascIIChar = ord(char)

            if operators[OpIndex] == "+":
                key += ascIIChar
            elif operators[OpIndex] == "-":
                key -= ascIIChar
            elif operators[OpIndex] == "*":
                key *= ascIIChar
        return key

    def __Rehash(self,username):
        '''Reshuffles the order of the operations in order to generate
        a unique key if a collision occurs'''
        key = 0
        for char in username:
            index = username.index(char)
            OpIndex = index % 3
            operators = ['+', '-', '*']
            random.shuffle(operators)
            ascIIChar = ord(char)

            if operators[OpIndex] == "+":
                key += ascIIChar
            elif operators[OpIndex] == "-":
                key -= ascIIChar
            elif operators[OpIndex] == "*":
                key *= ascIIChar
        return key

    def __sort(self, list):
        '''alreadyInOrder = 0
        inOrder = False
        while inOrder == False:
            for data in list:
                IndexPointer = list.index(data)
                if IndexPointer != len(list) - 1:
                    if list[IndexPointer] > list[IndexPointer + 1]:
                        tempV = list[IndexPointer]
                        list[IndexPointer] = list[IndexPointer + 1]
                        list[IndexPointer] = tempV
                    else:
                        alreadyInOrder += 1

            if alreadyInOrder == len(list):
                inOrder = True'''

        list = list.sort()

        return list


    def __FindMatchingKey(self, key, userIDs):
        '''Checks if a key inputted maps any of the other values in a
        list using binary search'''
        userTree = Tree(userIDs)
        found = userTree.Search(key)

        return found

    def __CheckSignInDetails(self, event, login):
        username = login[0]
        password = login[1]
        '''Checks all the userIDs to ensure that the username is
        valid and that the passsword maps to the username'''
        key = self.__GenerateUsernameKey(username)
        txt = "Login details are incorrect"
        from DataHandler import DataHandler
        dataHandler = DataHandler()
        userIDs = dataHandler.getUserIDs()
        found = self.__FindMatchingKey(key, userIDs)
        print(found)
        if found == False:
            self.__DisplayError(txt)
            return False

        user = dataHandler.getDetaForLogin(key)
        print(user)
        myUser = User(user)
        if user[0][2] != password:
            self.__DisplayError(txt)
        else:
            Main(self.window, self.sizings, myUser)
            
    def __CheckSignUpDetails(self, event, username, password, passwordR):

        '''Checks if the username matches and if the password is long enough'''
        unb = 'Username must not be blank'
        uun = 'Username is already taken'
        txt ='Please select a password that is at least 6 digits long'
        pdm = 'Password do not match'

        if username.strip(" ") == "":
            self.__DisplayError(unb)
            return

        key = self.__GenerateUsernameKey(username)
        ""

        from DataHandler import DataHandler
        self.dataHandler = DataHandler()
        b = self.dataHandler .getUserIDs()
        print(b)
        userIDs = b
        found = self.__FindMatchingKey(key, userIDs)
        if found == True:
            self.__DisplayError(uun)

        if len(password) < 6:
            self.__DisplayError(txt)
            return False

        if password != passwordR:
            self.__DisplayError(pdm)
            return False

        self.dataHandler.addUserDetails(key, username, password)
        user = [[key, username, password, 0]]
        myUser = User(user)
        Main(self.window, self.sizings, myUser)

    def __DisplayError(self, text):
        '''Displays Error at the bottom of the frame based on the situation'''
        fontStyle = (self.sizings.FontFamily[0], self.sizings.FontSize[7])
        errorWidget = Label(self.LoginFrame, text=text, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground2(), font=fontStyle)
        errorWidget.place(relx=0, rely=.9)

        errorWidget.after(2500, lambda: self.__RemoveErrorDisplay(errorWidget))

    def __RemoveErrorDisplay(self, widget):
        widget.destroy()

class World(Slide):
    def __init__(self, window, sizeAdjust, imageURL, text, user, avatar="", type=""):
        super().__init__(self, window, sizeAdjust, imageURL, text, avatar, type)
        self.Type = "World"
        self.user = user

    def viewSlide(self):
        '''Method called to implement the slide'''
        self.backgroundLabel.place_forget()
        self.__SlideFrame.place(relx=0, rely=0, width=self.sizings.width, height=self.sizing.height)
        self.__ImplementSlides()

    def __ImplementSlide(self):
        BackgroundLabel = Label(self.__SlideFrame, image=PhotoImage(file=imageURL))
        BackgroundLabel.place(relx=0, rely=0, width= self.sizings.height, height= self.sizings.height)

        MessageBox = Text(self.__SlideFrame, cursor="hand2", bg=self.__Theme.getBackground1(),
                          font=(self.sizings.FontFamily, self.sizings.FontSize[4]))
        MessageBox.place(relx=.5625, rely=0, width=.4375*self.sizings.width, height=.9*self.sizings.height)

        MessageEntry = Text(self.__SlideFrame, cursor="hand2", bg=self.__Theme.getBackground1(),
                          font=(self.sizings.FontFamily, self.sizings.FontSize[4]))
        MessageEntry.place(relx=.9, rely=.5625, width=.4375*self.sizings.width, height=.1*self.sizings.height)

        Button1 = Button(self.__SlideFrame, bg=self.__Theme.getBackground1(), bd=0, cursor="hand2", command=lambda:self.__Return(1))
        Button1.place(relx=0, rely=0, width=.2*self.sizings.width, height=(1/3)*self.sizings.height)

        Button2 = Button(self.__SlideFrame, bg=self.__Theme.getBackground1(), bd=0, cursor="hand2", command=lambda:self.__Return(2))
        Button2.place(relx=0, rely=0, width=.8*self.sizings.width, height=(1/3)*self.sizings.height)

        Button3 = Button(self.__SlideFrame, bg=self.__Theme.getBackground1(), bd=0, cursor="hand2", command=lambda: self.__Return(3))
        Button3.place(relx=0, rely=0, width=.2*self.sizings.width, height=(2/3)*self.sizings.height)

        Button4 = Button(self.__SlideFrame, bg=self.__Theme.getBackground1(), bd=0, cursor="hand2", command=lambda: self.__Return(4))
        Button4.place(relx=0, rely=0, width=.8*self.sizings.width, height=(2/3)*self.sizings.height)
        
    def __Return(self, value):
        return value

class Car:
    def __init__(self, canvas, imgURL, xPos, yPos):
        self.__canvas = canvas
        self.__imgURL = imgURL
        self.__xPos, self.__yPos = xPos, yPos
        threading.Thread(target=self.__createCar(), args=()).start()

    def __createCar(self):
        photoImage = PhotoImage(file=self.__imgURL)
        self.__canvas.image = photoImage
        self.__carNode = self.__canvas.create_image(self.__xPos, self.__yPos, image=photoImage)

        self.__canvas.update()

    def moveCar(self, dx):
        self.__xPos += dx
        self.__canvas.move(self.__carNode, dx, 0)
        self.__canvas.update()
        


class Game(Slide):
    def __init__(self, window, sizeAdjust):
        self.SlideFrame = Frame(window, bg=self.__Theme.getBackground1(), bd=0)
        self.sizings = sizeAdjust
        self.done = False

        self.DirectoryHandler = DirectoryHandler()
        print("DIRECTORY AT POINT OF CLASS:", os.getcwd())

class GameRunaway(Game):
    def __init__(self, window, sizeAdjust):
        #self.Type = "Welcome"

        super(GameRunaway, self).__init__(window, sizeAdjust)
        self.Stop = False
        self.lives = 5
        self.viewSlide()


    def viewSlide(self):
        print("DIRECTORY AT viewSlide", os.getcwd())
        self.SlideFrame.place(relx=0, rely=0, width=self.sizings.width, height=self.sizings.height)
        threading.Thread(target=self.__ImplementSlide(), args=()).start()

    def __ImplementSlide(self):
        self.BackgroundCanvas = Canvas(self.SlideFrame, bg="black")
        self.BackgroundCanvas.place(relx=0, rely=0, width=self.sizings.width, height=self.sizings.height)

        self.DirectoryHandler.changeDirectoryToBackgroundGame()
        backgroundImage = PhotoImage(file="road.png")

        self.RoadPos = -0.5 * self.sizings.width
        self.Road = self.BackgroundCanvas.create_image(self.RoadPos, self.sizings.height / 2 , image=backgroundImage)

        self.BackgroundCanvas.image = backgroundImage

        self.DirectoryHandler.changeDirectoryToMain()



        self.DirectoryHandler = DirectoryHandler()
        print(os.getcwd())
        self.DirectoryHandler.changeDirectoryToGameProps()

        playerX = self.sizings.width * 0.5
        chaserX = self.sizings.width * 0.05

        self.playerCar = Car(self.BackgroundCanvas, "racecar1.png", playerX, self.sizings.height // 2)
        #self.chaserCar = Car(self.BackgroundCanvas, "racecar2.png", chaserX, self.sizings.height // 2)



        threading.Thread(target=self.createInfoFrame(), args=()).start()
        threading.Thread(target=self.moveRoad(), args=()).start()
        threading.Thread(target=self.DirectoryHandler.changeDirectoryToMain(), args=()).start()

    def createInfoFrame(self):

        questionTheme = "white"
        questionTheme2 = "black"

        InfoFrame = Frame(self.SlideFrame, bg=questionTheme)
        InfoFrame.place(relx=0.6, rely=0,  width=.4* self.sizings.width, height=self.sizings.height)

        InfoTitle = Label(InfoFrame, text="Question", font=(self.sizings.FontFamily[1], self.sizings.FontSize[1]),
                          bg=questionTheme,fg=questionTheme2)
        InfoTitle.place(relx=.05, rely=.1 )

        QuestionPlaceHolder = Message(InfoFrame,
                                      font=(self.sizings.FontFamily[1], self.sizings.FontSize[5]), bg=questionTheme,
                                      fg=questionTheme2)
        QuestionPlaceHolder.place(relx=.05, rely=.35, width = self.sizings.width * .9, height=self.sizings.height * .15 )

        AnswerPlaceHolder = Entry(InfoFrame, font=(self.sizings.FontFamily[1], self.sizings.FontSize[6]),
                                  bg=questionTheme,fg=questionTheme2)
        AnswerPlaceHolder.place(relx=.2, rely=.65, width = self.sizings.width * .25)



        return True

    def moveRoad(self):
        while self.Stop == False:
            time.sleep(.05)
            oriBgPos = self.RoadPos
            self.RoadPos +=  0.025 * self.sizings.width
            if self.RoadPos>= 2.5:
                self.RoadPos = -0.5 * self.sizings.width

            change = self.RoadPos - oriBgPos

            self.BackgroundCanvas.move(self.Road, change, 0)
            self.BackgroundCanvas.update()




