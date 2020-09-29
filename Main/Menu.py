import tkinter
from tkinter import ttk
from Prompt import Prompt
from tkinter import *
from sizingAdjust import sizingAdjust
import os
import time
import math
import threading
from Tools.DirectoryHandler import DirectoryHandler
from Tools.DataHandler import DataHandler
from Tools.Theme import Theme
from Game import SwimmingGame
from Intro import SwimIntro
from Intro import BoardGameIntro
from Intro import BasketballIntro
from Intro import EllipseLessonIntro
from Intro import ProjectileLessonIntro
from Intro import MomentumLessonIntro
from Settings import Settings

class Main:
    def __init__(self, window, sizing, user):
        #Gathers neccessary attributes
        self.user = user
        self.DirectoryHandler = DirectoryHandler()
        self.DataHandler = DataHandler()

        self.__Theme = Theme()

        Fonts = [90, 80, 70, 60, 50, 40, 30, 20]
        self.FontFamily = ["Microsoft YaHei UI Light", "Ebrima"]

        self.InterfaceWindow = window

        #Collects neccesary sizing data and font data
        self.sizing = sizing
        self.padding = self.sizing.padding
        self.screenWidth = self.sizing.width
        self.screenHeight = self.sizing.height
        self.FontSize = self.sizing.FontSize

        #Creates screen canvas so canvas can be centred onto screens without a 16:9 screen ratio
        self.ScreenCanvas = Canvas(self.InterfaceWindow, borderwidth=0, highlightthickness=0)
        self.ScreenCanvas.place(relx=self.sizing.canvasPosX, rely=self.sizing.canvasPosY, width=self.screenWidth,
                                height=self.screenHeight)

        #Creates directory handler object to switch between directories
        self.DirectoryHandler = DirectoryHandler()
        self.DirectoryHandler.changeDirectoryToBackground()
        #Loads background
        StreetBackground = PhotoImage(file="backgroundImg1.png")
        self.DirectoryHandler.changeDirectoryToMain()

        #Displays background
        self.BackgroundLabel = Label(self.ScreenCanvas, image=StreetBackground, borderwidth=0, highlightthickness=0)
        self.BackgroundLabel.place(relx=-0.05, rely=-0.05)

        self.BackgroundPosX = -0.1
        self.BackgroundPosY = -0.1

        #Gets the user's username, coins, and its avatar
        username = self.user.getUsername()
        coins = self.user.getCoins()
        UserAvatar = self.user.getAvatar()
        AvatarURL = self.DataHandler.getAvatarURL(UserAvatar)

        self.DirectoryHandler.changeDirectoryToAvatar2()
        AvatarImage = PhotoImage(file=AvatarURL)
        self.DirectoryHandler.changeDirectoryToMain()


        LoginDetails = f'Username: {username}\nCoins: {coins}'


        self.AccountPlaceFrame = Frame(self.ScreenCanvas, bg=self.__Theme.getBackground1())
        self.AccountPlaceFrame.place(relx=.1, rely=.1, width = .8 *self.screenWidth,
                                height=(200/768)*self.screenHeight)

        AccountLabel = Label(self.AccountPlaceFrame)
        AccountLabel.place(relx=0, rely=0)

        AccountLabel['image'] = AvatarImage
        AccountLabel.config(image=AvatarImage)
        AccountLabel.image = AvatarImage


        loginDetailsFont = (self.FontFamily[0], self.FontSize[5])
        LoginDetailsMessage = Message(self.AccountPlaceFrame, text=LoginDetails, font=loginDetailsFont, bg=self.__Theme.getBackground1(),
                                      fg=self.__Theme.getForeground1(), width=int(round(1100*(self.screenWidth / 1366)))  )
        LoginDetailsMessage.place(relx=.225, rely=.05)


        #Displays quote to encourage students and some info in navigation to make life more easier
        fontStyle = (self.FontFamily[0], self.FontSize[7])
        self.quote = ["The roots of education are bitter, but the fruit is sweet.",
                 "Hint: When playing the basketball gme, click around the court for lessons/games",
                 "Press X to return to menu", "Hint: In the lessons move your arrow keys left and right to move forward",
                 "You can use your left and right keys to change option mentioned in the slideshow of game buttons"]

        self.QuoteIndex = -1

        self.QuoteText = Message(self.ScreenCanvas, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(),
                                 font = fontStyle, width= int(round((350* (self.screenWidth / 1366)))) )
        self.QuoteText.place(relx=0.55,rely=0.4, height=.5*self.screenHeight, width=.35*self.screenWidth)

        self.ChangeQuote()

        self.ButtonIndex = 0

        #Displays Buttons

        self.ButtonFrame = Frame(self.ScreenCanvas, bg=self.__Theme.getBackground1())
        self.ButtonFrame.place(relx=0.1, rely=0.4, width=.4*self.screenWidth, height=.5*self.screenHeight)

        buttonFont = (self.FontFamily[0], int(round(self.FontSize[7] * 1.5)))
        self.LeftButton = Button(self.ButtonFrame, text="<", bd=0, font=buttonFont, bg=self.__Theme.getBackground1(),
                                 fg=self.__Theme.getForeground1(), command=lambda: self.changeButtonIndex("-"))
        self.LeftButton.place(relx=.05, rely=.35)

        self.RightButton = Button(self.ButtonFrame, text=">", bd=0, font=buttonFont, bg=self.__Theme.getBackground1(),
                                 fg=self.__Theme.getForeground1(), command=lambda: self.changeButtonIndex("+"))
        self.RightButton.place(relx=.8, rely=.35)

        #Displays basketball game button
        #Switches directory
        self.DirectoryHandler.changeDirectoryToButton()
        #Creates photoimage for basketball button
        BasketballImage = PhotoImage(file="basketballBtn.png")
        #Returns directory back to norma.
        self.DirectoryHandler.changeDirectoryToMain()

        ##Creates basketball button
        self.BasketBallCourtButton = Button(self.ButtonFrame, image=BasketballImage, bd=0, cursor="hand2",
                                            highlightthickness=0,
                                            command= lambda: self.StartBasketballGame())
        #Displays button
        self.BasketBallCourtButton.place(relx=.2, rely=.1)


        #Switches directory to appropiate one
        self.DirectoryHandler.changeDirectoryToButton()
        #Loads swimming button game
        SwimmingImage = PhotoImage(file="SwimmingGame.png")
        #Changes directory to the main
        self.DirectoryHandler.changeDirectoryToMain()

        #Creates swimming button
        self.SwimGameButton = Button(self.ButtonFrame, image=SwimmingImage, bd=0, cursor="hand2",
                                            highlightthickness=0,
                                     command=lambda: self.StartSwimGame())

        #Changes directory to /Images/Button
        self.DirectoryHandler.changeDirectoryToButton()
        #Creates PhotImage for QuestButton
        AdventureImage = PhotoImage(file="AdventureGame.png")
        #Changes directory back to 'original' directory
        self.DirectoryHandler.changeDirectoryToMain()

        #Creates Adventure Button
        self.AdventureButton = Button(self.ButtonFrame, image=AdventureImage, bd=0, cursor="hand2", highlightthickness=0,
                                      command=lambda: self.StartAdventureGame())

        #Creates Settings Button
        #Changes directory to /Images/Button
        self.DirectoryHandler.changeDirectoryToButton()
        #Loads photoImage to settings buttons image
        SettingsImage = PhotoImage(file="Settings.png")
        #Changes directory back to normal
        self.DirectoryHandler.changeDirectoryToMain()



        #Creates settings button
        self.SettingsButton = Button(self.ButtonFrame, image=SettingsImage, bd=0, cursor="hand2",
                                      command=lambda: self.StartSettings())

        self.Buttons = [self.BasketBallCourtButton, self.SwimGameButton, self.AdventureButton, self.SettingsButton]

        self.xPosB = 0.5 * self.screenWidth
        self.yPosB = 0.5 * self.screenHeight

        self.DirectoryHandler.changeDirectoryToButton()
        LogoutImage = PhotoImage(file="logOut.png")
        self.DirectoryHandler.changeDirectoryToMain()

        self.LogoutButton = Button(self.AccountPlaceFrame, image = LogoutImage, bg=self.__Theme.getBackground1(), cursor="hand2", bd=0,
                                   command=lambda: self.Logout(), highlightthickness=0, activebackground=self.__Theme.getBackground1())
        self.LogoutButton.place(relx=1-(200/ (.8*1366) ), rely=0)

        #Returns directory to main folder for accessibility
        self.DirectoryHandler.changeDirectoryToMainFolder()

        #Animation of background giving a 3D effect
        self.InterfaceWindow.bind("<Motion>", lambda event: self.animateBackground(event))
        self.InterfaceWindow.bind("<Button-1>", lambda event: self.BlankMethod(event))
        self.InterfaceWindow.bind("<Key>", lambda event: self.changeButtonIndexEvent(event))
        self.InterfaceWindow.bind("<Return>", lambda event: self.SelectOption(event))
        #Ensures window runs perfectly
        threading.Thread(target=self.InterfaceWindow.mainloop(), args=()).start()

    def Logout(self):
        promptMessage = ["Log me out!", "Are you sure you want to log off? By pressing proceed you will have to sign in again to play any of these games."]
        self.LogoutPrompt = Prompt(self.InterfaceWindow, self.sizing, self.user, promptMessage)
        self.waitForResponse()

    def waitForResponse(self):
        response = self.LogoutPrompt.getGoAhead()
        if response == None:
            self.InterfaceWindow.after(50, lambda: self.waitForResponse())
        elif response == True:
            self.Logout2()

    def Logout2(self):
        from Slide import Slide
        from Slide import LoginPage
        self.DirectoryHandler.changeDirectoryToMain()
        loginSlide = LoginPage(self.InterfaceWindow, self.sizing, "backgroundImg1.png")
        threading.Thread(target=loginSlide.viewSlide(), args=()).start()

    def ChangeQuote(self):
        self.QuoteIndex += 1


        if self.QuoteIndex > len(self.quote) - 1:
            self.QuoteIndex = 0

        self.QuoteText['text'] = f"{self.quote[self.QuoteIndex]}"

        self.QuoteText.after(3000, lambda: self.ChangeQuote())

    def changeButtonIndexEvent(self, event):
        if event.keysym == "Left":
            direction = "-"
        elif event.keysym == "Right":
            direction = "+"
        else:
            direction = None

        if direction != None:
            self.Buttons[self.ButtonIndex].place_forget()
            if direction == "-":
                self.ButtonIndex -= 1
            elif direction == "+":
                self.ButtonIndex += 1

            if self.ButtonIndex < 0:
                self.ButtonIndex = 3
            elif self.ButtonIndex > 3:
                self.ButtonIndex = 0

            self.Buttons[self.ButtonIndex].place(relx=.2, rely=.1)

    def SelectOption(self, event):
        if True:
            if self.ButtonIndex == 0:
                self.StartBasketballGame()
            elif self.ButtonIndex == 1:
                self.StartSwimGame()
            elif self.ButtonIndex == 2:
                self.StartAdventureGame()
            elif self.ButtonIndex == 3:
                self.StartSettings()


    def changeButtonIndex(self, direction):
        self.Buttons[self.ButtonIndex].place_forget()

        if direction == "-":
            self.ButtonIndex -= 1
        elif direction == "+":
            self.ButtonIndex += 1

        if self.ButtonIndex < 0:
            self.ButtonIndex = 3
        elif self.ButtonIndex > 3:
            self.ButtonIndex = 0

        self.Buttons[self.ButtonIndex].place(relx=.2, rely=.1)

    def animateBackground(self, event):

        self.limitX = 0.1
        self.limitY = 0.1
        xPos = event.x
        yPos = event.y

        dx = xPos - self.xPosB
        dy = yPos - self.yPosB

        i = 0.02

        if dx > 0 and dy > 0:
            x = self.BackgroundPosX - (0.01*i)
            y = self.BackgroundPosY - (0.1*i)

            if x >= -self.limitX and y <= -self.limitY:
                self.BackgroundLabel.place(relx=x, rely=y)
            else:
                return

            self.BackgroundPosX += (0.1 * i)
            self.BackgroundPosY -= (0.1 * i)

            return

        elif dx > 0 and dy < 0:
            x = self.BackgroundPosX + (0.01*i)
            y = self.BackgroundPosY - (0.1*i)

            if x < 0 and y < 0:
                self.BackgroundLabel.place(relx=x, rely=y)
            else:
                return

            self.BackgroundPosX += (0.1 * i)
            self.BackgroundPosY += (0.1 * i)
            return

        elif dx < 0 and dy > 0:
            x = self.BackgroundPosX - (0.1*i)
            y = self.BackgroundPosY + (0.1*i)

            if x > -self.limitX and y > -self.limitY:
                self.BackgroundLabel.place(relx=x, rely=y)
            else:
                return

            self.BackgroundPosX -= (0.1 * i)
            self.BackgroundPosY -= (0.1 * i)
            return

        elif dx < 0 and dy < 0:
            x = self.BackgroundPosX + (0.01*i)
            y = self.BackgroundPosY + (0.01*i)

            if  x > -self.limitX and y < 0:
                self.BackgroundLabel.place(relx=x, rely=y)
            else:
                return

            self.BackgroundPosX -= (0.1 * i)
            self.BackgroundPosY += (0.1 * i)
            return

        self.xPosB = xPos
        self.yPosB = yPos

    def PlaceBackground(self, x, y):
        self.BackgroundLabel.place(relx=x, rely=y)

    def StartSwimGame(self):
        self.InterfaceWindow.bind("<Key>", lambda event: self.BlankMethod(event))
        self.InterfaceWindow.bind("<Motion>", lambda event: self.BlankMethod(event))
        #Changes directory back to normal
        self.DirectoryHandler.changeDirectoryToMain()
        #Loads swimming game
        SwimIntro(self.InterfaceWindow, self.sizing, self.user)

    def StartBasketballGame(self):
        self.InterfaceWindow.bind("<Key>", lambda event: self.BlankMethod(event))
        self.InterfaceWindow.bind("<Motion>", lambda event: self.BlankMethod(event))
        #Changes directory back to normal
        self.DirectoryHandler.changeDirectoryToMain()
        #Loads basketball game
        BasketballCourt(self.InterfaceWindow, self.sizing, self.user)

    def StartAdventureGame(self):
        self.InterfaceWindow.bind("<Key>", lambda event: self.BlankMethod(event))
        self.InterfaceWindow.bind("<Motion>", lambda event: self.BlankMethod(event))
        #Changes directory back to normal
        self.DirectoryHandler.changeDirectoryToMain()
        #Loads adventure game
        BoardGameIntro(self.InterfaceWindow, self.sizing, self.user)

    def StartSettings(self):
        self.InterfaceWindow.bind("<Key>", lambda event: self.BlankMethod(event))
        self.InterfaceWindow.bind("<Motion>", lambda event: self.BlankMethod(event))
        #Sets directory back to normal
        self.DirectoryHandler.changeDirectoryToMain()
        #Where settings live
        Settings(self.InterfaceWindow, self.sizing, self.user)

    def BlankMethod(self, event):
        pass


class BasketballCourt:
    def __init__(self, window, sizing, user):
        # Gathers attributes
        self.__Theme = Theme()
        self.InterfaceWindow = window
        self.Fonts = [90, 80, 70, 60, 50, 40, 30, 20]
        self.FontFamily = ["Microsoft YaHei UI Light", "Ebrima", "Courier New"]
        self.user = user

        # Creates directory changing object
        self.DirectoryHandler = DirectoryHandler()

        self.sizing = sizing

        # Creates Frame for interface
        self.SlideFrame = Canvas(self.InterfaceWindow, bg=self.__Theme.getBackground4(), cursor="hand2")
        self.SlideFrame.place(relx=self.sizing.canvasPosX, rely=self.sizing.canvasPosY, width=self.sizing.width1,
                              height=self.sizing.height1)

        fontStyle = (self.FontFamily[0], self.Fonts[7])
        self.InstructionsMessage = Message(self.InterfaceWindow, bg=self.__Theme.getBackground3(), fg=self.__Theme.getForeground1(),
                                           font=fontStyle)
        self.InstructionsMessage.place(relx=.6, rely=.075, width=.4 * self.sizing.width1, height=.6 * sizing.height1)

        self.InstructionsMessage['text'] = "Click on:\n\n1. Momentum Lesson(3 Point Area)\n2. Projectile Lesson(Free Throw Area)\n3. Goal Post\n4.(Anywhere else)Basketball Game Quiz or press G\n\nPress X or click on the button below to return to Menu"

        fontStyle = (self.FontFamily[0], self.Fonts[7])
        self.ThreePointAreaLbl = Label(self.InterfaceWindow, text=" ✎ |  ELLIPSE LESSON", font=fontStyle,
                                       bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1())
        self.ThreePointAreaLbl.place(relx=.25, rely=.65)

        self.FreeThrowAreaLbl = Label(self.InterfaceWindow, text=" ✎ |  MOMENTUM LESSON", font=fontStyle,
                                      bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1())
        self.FreeThrowAreaLbl.place(relx=.25, rely=.4)

        self.GoalAreaLbl = Label(self.InterfaceWindow, text=" ✎ |  PROJECTILE LESSON", font=fontStyle,
                                 bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1())
        self.GoalAreaLbl.place(relx=.1, rely=.5)

        self.BasketballGame = Label(self.InterfaceWindow, text=" ⛹ |  PLAY BASKETBALL GAME", font=fontStyle,
                                    bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1())
        self.BasketballGame.place(relx=.25, rely=.8)

        moveBackButtonFont = (self.sizing.FontFamily[0], self.sizing.FontSize[6])
        self.MoveBackButton = Button(self.InterfaceWindow, text="☰  |  RETURN TO MENU",
                                     bg=self.__Theme.getBackground2(),
                                     fg=self.__Theme.getForeground1(), command=lambda: self.ReturnToMenu(),
                                     font=moveBackButtonFont, bd=0, activebackground=self.__Theme.getBackground2())
        self.MoveBackButton.place(relx=.6, rely=.675, height=.15 * self.sizing.height, width=.4 * self.sizing.width)

        #Displays court
        self.DrawCourt()

        self.PreviousWidget = None

        self.InterfaceWindow.bind("<Key>", lambda event: self.GoBack(event))

        threading.Thread(target=self.InterfaceWindow.mainloop(), args=()).start()

    def ReturnToMenu(self):
        from Menu import Main
        # Returns to menu
        Main(self.InterfaceWindow, self.sizing, self.user)

    def GoBack(self, event):
        if event.keysym.upper() == "G":
            BasketballIntro(self.InterfaceWindow, self.sizing, self.user)

        # Returns to menu
        if event.keysym.upper() == "X":
            from Menu import Main
            Main(self.InterfaceWindow, self.sizing, self.user)

    def DrawCourt(self):

        # Changes directory
        self.DirectoryHandler.changeDirectoryToBackgroundGameNA()
        # Sets photoImage of background of court
        photoImage = PhotoImage(file='basketballCourtBlank.png')

        # Generates geometrical positions
        bgPosX = int(round(self.sizing.width1 / 2))
        bgPosY = int(round(self.sizing.height1 / 2))

        # Places background at the exact position that will cover the whole screen
        self.Background = self.SlideFrame.create_image(bgPosX, bgPosY, image=photoImage)
        self.SlideFrame.image = photoImage
        self.DirectoryHandler.changeDirectoryToMain()

        PitchSideX1 = (1.08 / 32) * self.sizing.width1
        PitchSideY1 = (1.35 / 16) * self.sizing.height1
        PitchSideX2 = (16 / 32) * self.sizing.width1
        PitchSideY2 = (14.65 / 16) * self.sizing.height1

        self.PitchSideL = self.SlideFrame.create_rectangle(PitchSideX1, PitchSideY1, PitchSideX2, PitchSideY2, width=3,
                                                           outline=self.__Theme.getLineColour(),
                                                           fill=self.__Theme.getBackground4())

        PitchSideX1 = (16 / 32) * self.sizing.width1
        PitchSideY1 = (1.35 / 16) * self.sizing.height1
        PitchSideX2 = (32 - 1.08) * self.sizing.width1
        PitchSideY2 = (14.65 / 16) * self.sizing.height1

        self.PitchSideR = self.SlideFrame.create_rectangle(PitchSideX1, PitchSideY1, PitchSideX2, PitchSideY2, width=3,
                                                           outline=self.__Theme.getLineColour(),
                                                           fill=self.__Theme.getBackground4())

        CentreOfPitchX1 = (14 / 32) * self.sizing.width1
        CentreOfPitchY1 = (self.sizing.height1 / 2) - ((2 / 32) * self.sizing.width1)
        CentreOfPitchX2 = (18 / 32) * self.sizing.width1
        CentreOfPitchY2 = (self.sizing.height1 / 2) + ((2 / 32) * self.sizing.width1)

        self.Centre = self.SlideFrame.create_oval(CentreOfPitchX1, CentreOfPitchY1, CentreOfPitchX2, CentreOfPitchY2,
                                                  width=3,
                                                  outline=self.__Theme.getLineColour(),
                                                  fill=self.__Theme.getBackground4())

        GoalAreaX1 = (-9 / 32) * self.sizing.width1
        GoalAreaY1 = (2.5 / 18) * self.sizing.height1

        GoalAreaX2 = (11 / 32) * self.sizing.width1
        GoalAreaY2 = (15.5 / 18) * self.sizing.height1

        self.GoalOvalL = self.SlideFrame.create_oval(GoalAreaX1, GoalAreaY1, GoalAreaX2, GoalAreaY2, width=3,
                                                     outline=self.__Theme.getLineColour(),
                                                     fill=self.__Theme.getBackground4())

        GoalAreaX1 = (21 / 32) * self.sizing.width1
        GoalAreaX2 = (41 / 32) * self.sizing.width1

        self.GoalOvalR = self.SlideFrame.create_oval(GoalAreaX1, GoalAreaY1, GoalAreaX2, GoalAreaY2, width=3,
                                                     outline=self.__Theme.getLineColour(),
                                                     fill=self.__Theme.getBackground4())

        # GoalRect
        GoalRectX1L = (1.00 / 32) * self.sizing.width1
        GoalRectX2L = (7.25 / 32) * self.sizing.width1
        GoalRectX1R = (24.75 / 32) * self.sizing.width1
        GoalRectX2R = (31.0 / 32) * self.sizing.width1

        GoalRectY1 = (6.50 / 18) * self.sizing.height1
        GoalRectY2 = (11.5 / 18) * self.sizing.height1

        self.GoalRectL = self.SlideFrame.create_rectangle(GoalRectX1L, GoalRectY1, GoalRectX2L, GoalRectY2,
                                                          outline=self.__Theme.getLineColour(), width=3,
                                                          fill=self.__Theme.getBackground4())
        self.GoalRectR = self.SlideFrame.create_rectangle(GoalRectX1R, GoalRectY1, GoalRectX2R, GoalRectY2,
                                                          outline=self.__Theme.getLineColour(), width=3,
                                                          fill=self.__Theme.getBackground4())

        # Circle Connecting to Rectangle
        GoalCircleX1L = (4.750 / 32) * self.sizing.width1
        GoalCircleX2L = (9.750 / 32) * self.sizing.width1

        GoalCircleX1R = (22.25 / 32) * self.sizing.width1
        GoalCircleX2R = (27.25 / 32) * self.sizing.width1

        GoalCircleY1 = (6.50 / 18) * self.sizing.height1
        GoalCircleY2 = (11.5 / 18) * self.sizing.height1

        # self.GoalRectL.tag_lower()
        # self.GoalRectR.tag_lower()

        self.CircleL = self.SlideFrame.create_oval(GoalCircleX1L, GoalCircleY1, GoalCircleX2L, GoalCircleY2,
                                                   outline=self.__Theme.getLineColour(), width=3,
                                                   fill=self.__Theme.getBackground4())
        self.CircleR = self.SlideFrame.create_oval(GoalCircleX1R, GoalCircleY1, GoalCircleX2R, GoalCircleY2,
                                                   outline=self.__Theme.getLineColour(), width=3,
                                                   fill=self.__Theme.getBackground4())

        # Goal
        GoalPostL1X = (1.5 / 32) * self.sizing.width1
        GoalPostL2X = (1.5 / 32) * self.sizing.width1

        GoalNetL1X = (1.50 / 32) * self.sizing.width1
        GoalNetL2X = (3.75 / 32) * self.sizing.width1

        GoalPostR1X = (30.5 / 32) * self.sizing.width1
        GoalPostR2X = (30.5 / 32) * self.sizing.width1

        GoalNetR1X = (28.25 / 32) * self.sizing.width1
        GoalNetR2X = (30.50 / 32) * self.sizing.width1

        Goal1Y = (7.875 / 18) * self.sizing.height1
        Goal2Y = (10.125 / 18) * self.sizing.height1

        #   a) Goal Line
        self.GoalLineL = self.SlideFrame.create_line(GoalPostL1X, Goal1Y, GoalPostL2X, Goal2Y,
                                                     fill=self.__Theme.getLineColour(), width=3)
        self.GoalLineR = self.SlideFrame.create_line(GoalPostR1X, Goal1Y, GoalPostR2X, Goal2Y,
                                                     fill=self.__Theme.getLineColour(), width=3)

        #   b) Goal Circle
        self.GoalCircleL = self.SlideFrame.create_oval(GoalNetL1X, Goal1Y, GoalNetL2X, Goal2Y,
                                                       fill=self.__Theme.getBackground4(),
                                                       outline=self.__Theme.getLineColour(), width=3)
        self.GoalCircleR = self.SlideFrame.create_oval(GoalNetR1X, Goal1Y, GoalNetR2X, Goal2Y,
                                                       fill=self.__Theme.getBackground4(),
                                                       outline=self.__Theme.getLineColour(), width=3)

        # Create rectangle to cover the other half of the ovals
        blankX2L = (1.0 / 32) * self.sizing.width1
        blankX2R = (31.0 / 32) * self.sizing.width1
        blankX2R2 = self.sizing.width1
        blankY = self.sizing.height1

        self.SlideFrame.create_rectangle(0, 0, blankX2L, blankY, fill=self.__Theme.getBackground4(), width=0)
        self.SlideFrame.create_rectangle(blankX2R, 0, blankX2R2, blankY, fill=self.__Theme.getBackground4(), width=0)

        x1 = (1 / 32) * self.sizing.width1
        y1 = (1.5 / 18) * self.sizing.height1
        x2 = (31 / 32) * self.sizing.width1
        y2 = (16.5 / 18) * self.sizing.height1

        self.SlideFrame.create_line(x1, y1, x1, y2, fill=self.__Theme.getLineColour(), width=3)
        self.SlideFrame.create_line(x2, y1, x2, y2, fill=self.__Theme.getLineColour(), width=3)

        self.SlideFrame.update()

        self.SlideFrame.bind("<Button-1>", lambda event: self.SelectOption(event))
        self.SlideFrame.bind("<Motion>", lambda event: self.HoverOption(event))

    def ExitOption(self):
        # Detects what widget was being pressed and from there takes the user to a part of the game
        self.ThreePointAreaLbl.place(relx=.25, rely=.65)
        # DISPLAYS FREE THROW AREA
        self.FreeThrowAreaLbl.place(relx=.25, rely=.4)
        # DISPLAYS GOAL POST
        self.GoalAreaLbl.place(relx=.1, rely=.5)
        # DISPLAYS BASKETBALL GAME
        self.BasketballGame.place(relx=.25, rely=.8)

    def HoverOption(self, event):
        # Detects what widget was being pressed and from there takes the user to a part of the game
        if self.SlideFrame.find_withtag(CURRENT):
            a = self.SlideFrame.find_withtag(CURRENT)

            # print(a[0], self.PreviousWidget)

            if a[0] == 5:
                if self.PreviousWidget != a[0]:
                    # DISPLAYS 3 POINT AREA
                    self.ThreePointAreaLbl.place(relx=.25 + .02, rely=.65)
                    self.PreviousWidget = a[0]
            elif a[0] == 9:
                if self.PreviousWidget != a[0]:
                    # DISPLAYS FREE THROW AREA
                    self.FreeThrowAreaLbl.place(relx=.25 + .02, rely=.4)
                    self.PreviousWidget = a[0]

            elif a[0] == 13:
                if self.PreviousWidget != a[0]:
                    # DISPLAYS GOAL POST
                    self.GoalAreaLbl.place(relx=.1 + .02, rely=.5)
                    self.PreviousWidget = a[0]

            elif a[0] == 2:
                if self.PreviousWidget != a[0]:
                    # DISPLAYS BASKETBALL GAME
                    self.BasketballGame.place(relx=.25 + .02, rely=.8)
                    self.PreviousWidget = a[0]
            else:
                self.PreviousWidget = None
                return

        self.InterfaceWindow.after(1000, lambda: self.ExitOption())

    def SelectOption(self, event):
        # Detects what widget was being pressed and from there takes the user to a part of the game
        if self.SlideFrame.find_withtag(CURRENT):
            a = self.SlideFrame.find_withtag(CURRENT)
            if a[0] == 2:
                # DISPLAYS BASKETBALL GAME
                from Game import BGMain
                BasketballIntro(self.InterfaceWindow, self.sizing, self.user)
            if a[0] == 5:
                # DISPLAYS 3 POINT AREA
                EllipseLessonIntro(self.InterfaceWindow, self.sizing, self.user)

            elif a[0] == 9:
                # DISPLAYS FREE THROW AREA
                MomentumLessonIntro(self.InterfaceWindow, self.sizing, self.user)

            elif a[0] == 13:
                # DISPLAYS GOAL POST
                ProjectileLessonIntro(self.InterfaceWindow, self.sizing, self.user)

            else:
                pass

