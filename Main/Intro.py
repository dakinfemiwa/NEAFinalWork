from tkinter import ttk
from tkinter import *
from Tools.sizingAdjust import sizingAdjust
import os
import threading
from Game import BoardGame
from Game import SwimmingGame
from Game import BGMain
from Lesson import ProjectileLessonMain
from Lesson import MomentumLessonMain
from Lesson import EllipseLessonMain
from DirectoryHandler import DirectoryHandler
from Tools.story import SlideData
from Tools.story import Episode
from Tools.Theme import Theme

class EllipseLessonIntro:
    def __init__(self, window, sizings, user):
        #Generates neccsesary attributes
        self.Tasks = []
        self.user = user
        Fonts = [90, 80, 70, 60, 50, 40, 30, 20]
        self.FontFamily = ["Microsoft YaHei UI Light", "Ebrima"]
        self.interfaceDirectory = os.getcwd()
        padding = 80

        self.InterfaceWindow = window

        #Generates neccesary sizings
        sizing = sizings
        self.sizing = sizing
        self.padding = sizing.padding
        self.screenWidth = sizing.width
        self.screenHeight = sizing.height
        self.FontSize = sizing.FontSize
        self.DirectoryHandler = DirectoryHandler()
        self.__Theme = Theme()

        #Ensure canvas is in centre of screen
        self.ScreenCanvas = Frame(self.InterfaceWindow)
        self.ScreenCanvas.place(relx=sizing.canvasPosX, rely=sizing.canvasPosY, width=self.screenWidth,
                                height=self.screenHeight)

        self.DirectoryHandler.changeDirectoryToBackground()
        background = PhotoImage(file="gameIntro.png")
        self.DirectoryHandler.changeDirectoryToMain()

        BackgroundLabel = Label(self.ScreenCanvas, image=background)
        BackgroundLabel.place(relx=0, rely=0)

        self.ShowIntro()

        #Binds window so game can start at command
        self.InterfaceWindow.bind("<Key> ", lambda event: self.navigation(event))

        threading.Thread(target=self.InterfaceWindow.mainloop(), args=()).start()

    def navigation(self, event):
        if event.keysym.upper() == "X":
            self.ReturnToMenu()

    def ShowIntro(self):
        self.InfoFrame = Frame(self.ScreenCanvas, bg=self.__Theme.getBackground1())
        self.InfoFrame.place(relx=.1, rely=.1, width=.8*self.sizing.width, height=.8*self.sizing.height)

        fontStyle = (self.FontFamily[0], self.FontSize[0])
        GameTitleLabel = Message(self.InfoFrame, text="Lesson- Ellipses", font=fontStyle, bg=self.__Theme.getBackground1(),
                                 fg=self.__Theme.getForeground1(), width=int(round(650 * (self.sizing.width /1366))))
        GameTitleLabel.place(relx=0, rely=0, width=.6 *self.sizing.width, height=.6*self.sizing.height)

        fontStyle = (self.FontFamily[0], self.FontSize[7])
        episodeInfo = "How can such interesting shpaes be used in basketball?"
        self.GameDescriptionLabel = Message(self.InfoFrame, text=episodeInfo, font=fontStyle,
                                     bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(),
                                       width = int(round(600 * (self.sizing.width / 1366))))
        self.GameDescriptionLabel.place(relx=0, rely=.7, width=.6 * self.sizing.width, height=.2*self.sizing.height)

        moveBackButtonFont = (self.sizing.FontFamily[0], self.sizing.FontSize[5])
        self.MoveBackButton = Button(self.InfoFrame, text="EXIT", bg=self.__Theme.getBackground2(), cursor="hand2",
                                     fg=self.__Theme.getForeground1(), command=lambda: self.ReturnToMenu(),
                                     font=moveBackButtonFont, bd=0, activebackground=self.__Theme.getBackground2())
        self.MoveBackButton.place(relx=.8, rely=.505, height=.8*.15*self.sizing.height, width=.8*.15*self.sizing.width)

        self.PlayGameButton = Button(self.InfoFrame, text="LEARN", bg=self.__Theme.getBackground2(),
                                     fg=self.__Theme.getForeground1(), cursor="hand2",
                                     font=moveBackButtonFont, bd=0, activebackground=self.__Theme.getBackground2())
        self.PlayGameButton.place(relx=.8, rely=.345, height=.8*.15*self.sizing.height, width=.8*.15*self.sizing.width)

        self.InterfaceWindow.bind("<Button-1>", lambda event: self.LoadGame(event))
        self.InterfaceWindow.bind("<Key>", lambda event: self.LoadGame(event))

    def LoadGame(self, event):
        if event.widget == self.PlayGameButton:
            self.GameDescriptionLabel['text'] = "Loading game..."
            self.InterfaceWindow.after(3000, lambda: self.__Load())

    def __Load(self):
        self.PlayGameButton.destroy()
        EllipseLessonMain(self.InterfaceWindow, self.sizing, self.user)

    def ReturnToMenu(self):
        from Menu import Main
        # Returns to menu
        from Menu import BasketballCourt
        BasketballCourt(self.InterfaceWindow, self.sizing, self.user)

class MomentumLessonIntro:
    def __init__(self, window, sizings, user):
        #Generates neccsesary attributes
        self.Tasks = []
        self.user = user
        Fonts = [90, 80, 70, 60, 50, 40, 30, 20]
        self.FontFamily = ["Microsoft YaHei UI Light", "Ebrima"]
        self.interfaceDirectory = os.getcwd()
        padding = 80

        self.InterfaceWindow = window

        #Generates neccesary sizings
        sizing = sizings
        self.sizing = sizing
        self.padding = sizing.padding
        self.screenWidth = sizing.width
        self.screenHeight = sizing.height
        self.FontSize = sizing.FontSize
        self.DirectoryHandler = DirectoryHandler()
        self.__Theme = Theme()

        #Ensure canvas is in centre of screen
        self.ScreenCanvas = Frame(self.InterfaceWindow)
        self.ScreenCanvas.place(relx=sizing.canvasPosX, rely=sizing.canvasPosY, width=self.screenWidth,
                                height=self.screenHeight)

        self.DirectoryHandler.changeDirectoryToBackground()
        background = PhotoImage(file="gameIntro.png")
        self.DirectoryHandler.changeDirectoryToMain()

        BackgroundLabel = Label(self.ScreenCanvas, image=background)
        BackgroundLabel.place(relx=0, rely=0)

        self.ShowIntro()

        #Binds window so game can start at command
        self.InterfaceWindow.bind("<Key> ", lambda event: self.navigation(event))

        threading.Thread(target=self.InterfaceWindow.mainloop(), args=()).start()

    def navigation(self, event):
        if event.keysym.upper() == "X":
            self.ReturnToMenu()

    def ShowIntro(self):
        self.InfoFrame = Frame(self.ScreenCanvas, bg=self.__Theme.getBackground1())
        self.InfoFrame.place(relx=.1, rely=.1, width=.8*self.sizing.width, height=.8*self.sizing.height)

        fontStyle = (self.FontFamily[0], self.FontSize[0])
        GameTitleLabel = Message(self.InfoFrame, text="LESSON- MOMENTUM", font=fontStyle, bg=self.__Theme.getBackground1(),
                                 fg=self.__Theme.getForeground1(), width=int(round(850 * (self.sizing.width /1366))))
        GameTitleLabel.place(relx=0, rely=0, width=.65 *self.sizing.width, height=.6*self.sizing.height)

        fontStyle = (self.FontFamily[0], self.FontSize[7])
        episodeInfo = "What is momentum?"
        self.GameDescriptionLabel = Message(self.InfoFrame, text=episodeInfo, font=fontStyle,
                                     bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(),
                                       width = int(round(600 * (self.sizing.width / 1366))))
        self.GameDescriptionLabel.place(relx=0, rely=.7, width=.6 * self.sizing.width, height=.2*self.sizing.height)

        moveBackButtonFont = (self.sizing.FontFamily[0], self.sizing.FontSize[5])
        self.MoveBackButton = Button(self.InfoFrame, text="EXIT", bg=self.__Theme.getBackground2(), cursor="hand2",
                                     fg=self.__Theme.getForeground1(), command=lambda: self.ReturnToMenu(),
                                     font=moveBackButtonFont, bd=0, activebackground=self.__Theme.getBackground2())
        self.MoveBackButton.place(relx=.8, rely=.505, height=.8*.15*self.sizing.height, width=.8*.15*self.sizing.width)

        self.PlayGameButton = Button(self.InfoFrame, text="LEARN", bg=self.__Theme.getBackground2(),
                                     fg=self.__Theme.getForeground1(), cursor="hand2",
                                     font=moveBackButtonFont, bd=0, activebackground=self.__Theme.getBackground2())
        self.PlayGameButton.place(relx=.8, rely=.345, height=.8*.15*self.sizing.height, width=.8*.15*self.sizing.width)

        self.InterfaceWindow.bind("<Button-1>", lambda event: self.LoadGame(event))
        self.InterfaceWindow.bind("<Key>", lambda event: self.LoadGame(event))

    def LoadGame(self, event):
        if event.widget == self.PlayGameButton:
            self.GameDescriptionLabel['text'] = "Loading game..."
            self.InterfaceWindow.after(3000, lambda: self.__Load())

    def __Load(self):
        self.PlayGameButton.destroy()
        MomentumLessonMain(self.InterfaceWindow, self.sizing, self.user)

    def ReturnToMenu(self):
        from Menu import Main
        # Returns to menu
        from Menu import BasketballCourt
        BasketballCourt(self.InterfaceWindow, self.sizing, self.user)

class ProjectileLessonIntro:
    def __init__(self, window, sizings, user):
        #Generates neccsesary attributes
        self.Tasks = []
        self.user = user
        Fonts = [90, 80, 70, 60, 50, 40, 30, 20]
        self.FontFamily = ["Microsoft YaHei UI Light", "Ebrima"]
        self.interfaceDirectory = os.getcwd()
        padding = 80

        self.InterfaceWindow = window

        #Generates neccesary sizings
        sizing = sizings
        self.sizing = sizing
        self.padding = sizing.padding
        self.screenWidth = sizing.width
        self.screenHeight = sizing.height
        self.FontSize = sizing.FontSize
        self.DirectoryHandler = DirectoryHandler()
        self.__Theme = Theme()

        #Ensure canvas is in centre of screen
        self.ScreenCanvas = Frame(self.InterfaceWindow)
        self.ScreenCanvas.place(relx=sizing.canvasPosX, rely=sizing.canvasPosY, width=self.screenWidth,
                                height=self.screenHeight)

        self.DirectoryHandler.changeDirectoryToBackground()
        background = PhotoImage(file="gameIntro.png")
        self.DirectoryHandler.changeDirectoryToMain()

        BackgroundLabel = Label(self.ScreenCanvas, image=background)
        BackgroundLabel.place(relx=0, rely=0)

        self.ShowIntro()

        #Binds window so game can start at command
        self.InterfaceWindow.bind("<Key> ", lambda event: self.navigation(event))

        threading.Thread(target=self.InterfaceWindow.mainloop(), args=()).start()

    def navigation(self, event):
        if event.keysym.upper() == "X":
            self.ReturnToMenu()

    def ShowIntro(self):
        self.InfoFrame = Frame(self.ScreenCanvas, bg=self.__Theme.getBackground1())
        self.InfoFrame.place(relx=.1, rely=.1, width=.8*self.sizing.width, height=.8*self.sizing.height)

        fontStyle = (self.FontFamily[0], self.FontSize[0])
        GameTitleLabel = Message(self.InfoFrame, text="LESSON- PROJECTILE", font=fontStyle, bg=self.__Theme.getBackground1(),
                                 fg=self.__Theme.getForeground1(), width=int(round(650 * (self.sizing.width /1366))))
        GameTitleLabel.place(relx=0, rely=0, width=.6 *self.sizing.width, height=.6*self.sizing.height)

        fontStyle = (self.FontFamily[0], self.FontSize[7])
        episodeInfo = "Learn about projectile Motion"
        self.GameDescriptionLabel = Message(self.InfoFrame, text=episodeInfo, font=fontStyle,
                                     bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(),
                                       width = int(round(600 * (self.sizing.width / 1366))))
        self.GameDescriptionLabel.place(relx=0, rely=.7, width=.6 * self.sizing.width, height=.2*self.sizing.height)

        moveBackButtonFont = (self.sizing.FontFamily[0], self.sizing.FontSize[5])
        self.MoveBackButton = Button(self.InfoFrame, text="EXIT", bg=self.__Theme.getBackground2(), cursor="hand2",
                                     fg=self.__Theme.getForeground1(), command=lambda: self.ReturnToMenu(),
                                     font=moveBackButtonFont, bd=0, activebackground=self.__Theme.getBackground2())
        self.MoveBackButton.place(relx=.8, rely=.505, height=.8*.15*self.sizing.height, width=.8*.15*self.sizing.width)

        self.PlayGameButton = Button(self.InfoFrame, text="LEARN", bg=self.__Theme.getBackground2(),
                                     fg=self.__Theme.getForeground1(), cursor="hand2",
                                     font=moveBackButtonFont, bd=0, activebackground=self.__Theme.getBackground2())
        self.PlayGameButton.place(relx=.8, rely=.345, height=.8*.15*self.sizing.height, width=.8*.15*self.sizing.width)

        self.InterfaceWindow.bind("<Button-1>", lambda event: self.LoadGame(event))
        self.InterfaceWindow.bind("<Key>", lambda event: self.LoadGame(event))

    def LoadGame(self, event):
        if event.widget == self.PlayGameButton:
            self.GameDescriptionLabel['text'] = "Loading game..."
            self.InterfaceWindow.after(3000, lambda: self.__Load())

    def __Load(self):
        ProjectileLessonMain(self.InterfaceWindow, self.sizing, self.user)

    def ReturnToMenu(self):
        from Menu import Main
        # Returns to menu
        from Menu import BasketballCourt
        BasketballCourt(self.InterfaceWindow, self.sizing, self.user)

class BasketballIntro:
    def __init__(self, window, sizings, user):
        #Generates neccsesary attributes
        self.Tasks = []
        self.user = user
        Fonts = [90, 80, 70, 60, 50, 40, 30, 20]
        self.FontFamily = ["Microsoft YaHei UI Light", "Ebrima"]
        self.interfaceDirectory = os.getcwd()
        padding = 80

        self.InterfaceWindow = window

        #Generates neccesary sizings
        sizing = sizings
        self.sizing = sizing
        self.padding = sizing.padding
        self.screenWidth = sizing.width
        self.screenHeight = sizing.height
        self.FontSize = sizing.FontSize
        self.DirectoryHandler = DirectoryHandler()
        self.__Theme = Theme()

        #Ensure canvas is in centre of screen
        self.ScreenCanvas = Frame(self.InterfaceWindow)
        self.ScreenCanvas.place(relx=sizing.canvasPosX, rely=sizing.canvasPosY, width=self.screenWidth,
                                height=self.screenHeight)

        self.DirectoryHandler.changeDirectoryToBackground()
        background = PhotoImage(file="basketballBackground.png")
        self.DirectoryHandler.changeDirectoryToMain()

        BackgroundLabel = Label(self.ScreenCanvas, image=background)
        BackgroundLabel.place(relx=0, rely=0)

        self.ShowIntro()

        #Binds window so game can start at command
        self.InterfaceWindow.bind("<Key> ", lambda event: self.navigation(event))

        threading.Thread(target=self.InterfaceWindow.mainloop(), args=()).start()

    def navigation(self, event):
        if event.keysym.upper() == "X":
            self.ReturnToMenu()

    def ShowIntro(self):
        self.InfoFrame = Frame(self.ScreenCanvas, bg=self.__Theme.getBackground1())
        self.InfoFrame.place(relx=.1, rely=.1, width=.8*self.sizing.width, height=.8*self.sizing.height)

        fontStyle = (self.FontFamily[0], self.FontSize[0])
        GameTitleLabel = Message(self.InfoFrame, text="GAME - Basketball", font=fontStyle, bg=self.__Theme.getBackground1(),
                                 fg=self.__Theme.getForeground1(), width=int(round(650 * (self.sizing.width /1366))))
        GameTitleLabel.place(relx=0, rely=0, width=.6 *self.sizing.width, height=.6*self.sizing.height)

        fontStyle = (self.FontFamily[0], int(round(1 * self.FontSize[7])))
        episodeInfo = "Shoot the ball in the lane corresponding to the correct answer. You have 5 balls so use them wisely!"
        self.GameDescriptionLabel = Message(self.InfoFrame, text=episodeInfo, font=fontStyle,
                                     bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(),
                                       width = int(round(600 * (self.sizing.width / 1366))))
        self.GameDescriptionLabel.place(relx=0, rely=.7, width=.6 * self.sizing.width, height=.2*self.sizing.height)

        moveBackButtonFont = (self.FontFamily[0], int(round(self.FontSize[7])))
        self.MoveBackButton = Button(self.InfoFrame, text="EXIT", bg=self.__Theme.getBackground2(), cursor="hand2",
                                     fg=self.__Theme.getForeground1(), command=lambda: self.ReturnToMenu(),
                                     font=moveBackButtonFont, bd=0, activebackground=self.__Theme.getBackground2())
        self.MoveBackButton.place(relx=.8, rely=.665, height=.8*.15*self.sizing.height, width=.8*.15*self.sizing.width)

        self.HardButton = Button(self.InfoFrame, text="HARD", bg=self.__Theme.getBackground2(),
                                     fg=self.__Theme.getForeground1(), cursor="hand2",
                                     font=moveBackButtonFont, bd=0, activebackground=self.__Theme.getBackground2())
        self.HardButton.place(relx=.8, rely=.505, height=.8*.15*self.sizing.height, width=.8*.15*self.sizing.width)

        self.MediumButton = Button(self.InfoFrame, text="MEDIUM", bg=self.__Theme.getBackground2(),
                                     fg=self.__Theme.getForeground1(), cursor="hand2",
                                     font=moveBackButtonFont, bd=0, activebackground=self.__Theme.getBackground2())
        self.MediumButton.place(relx=.8, rely=.345, height=.8*.15*self.sizing.height, width=.8*.15*self.sizing.width)

        self.EasyButton = Button(self.InfoFrame, text="EASY", bg=self.__Theme.getBackground2(),
                                     fg=self.__Theme.getForeground1(), cursor="hand2",
                                     font=moveBackButtonFont, bd=0, activebackground=self.__Theme.getBackground2())
        self.EasyButton.place(relx=.8, rely=.185, height=.8*.15*self.sizing.height, width=.8*.15*self.sizing.width)

        self.InterfaceWindow.bind("<Button-1>", lambda event: self.LoadGame(event))
        self.InterfaceWindow.bind("<Key>", lambda event: self.LoadGame(event))

    def LoadGame(self, event):
        if event.widget == self.EasyButton:
            self.GameDescriptionLabel['text'] = "Loading game..."
            self.InterfaceWindow.after(3000, lambda: self.__Load("Easy"))
        elif event.widget == self.MediumButton:
            self.GameDescriptionLabel['text'] = "Loading game..."
            self.InterfaceWindow.after(3000, lambda: self.__Load("Medium"))
        elif event.widget == self.HardButton:
            self.GameDescriptionLabel['text'] = "Loading game..."
            self.InterfaceWindow.after(3000, lambda: self.__Load("Hard"))

    def __Load(self, difficulty):
        self.ScreenCanvas.destroy()
        BGMain(self.InterfaceWindow, self.sizing, self.user, difficulty)

    def ReturnToMenu(self):
        from Menu import Main
        # Returns to menu
        from Menu import BasketballCourt
        BasketballCourt(self.InterfaceWindow, self.sizing, self.user)

class SwimIntro:
    def __init__(self, window, sizings, user):
        #Generates neccsesary attributes
        self.Tasks = []
        self.user = user
        Fonts = [90, 80, 70, 60, 50, 40, 30, 20]
        self.FontFamily = ["Microsoft YaHei UI Light", "Ebrima"]
        self.interfaceDirectory = os.getcwd()
        padding = 80

        self.InterfaceWindow = window

        #Generates neccesary sizings
        sizing = sizings
        self.sizing = sizing
        self.padding = sizing.padding
        self.screenWidth = sizing.width
        self.screenHeight = sizing.height
        self.FontSize = sizing.FontSize
        self.DirectoryHandler = DirectoryHandler()
        self.__Theme = Theme()

        #Ensure canvas is in centre of screen
        self.ScreenCanvas = Frame(self.InterfaceWindow)
        self.ScreenCanvas.place(relx=sizing.canvasPosX, rely=sizing.canvasPosY, width=self.screenWidth,
                                height=self.screenHeight)

        self.DirectoryHandler.changeDirectoryToBackground()
        background = PhotoImage(file="swimming.png")
        self.DirectoryHandler.changeDirectoryToMain()

        BackgroundLabel = Label(self.ScreenCanvas, image=background)
        BackgroundLabel.place(relx=0, rely=0)

        self.ShowIntro()

        #Binds window so game can start at command
        self.InterfaceWindow.bind("<Key> ", lambda event: self.navigation(event))

        threading.Thread(target=self.InterfaceWindow.mainloop(), args=()).start()

    def navigation(self, event):
        if event.keysym.upper() == "X":
            self.ReturnToMenu()

    def ShowIntro(self):
        self.InfoFrame = Frame(self.ScreenCanvas, bg=self.__Theme.getBackground1())
        self.InfoFrame.place(relx=.1, rely=.1, width=.8*self.sizing.width, height=.8*self.sizing.height)

        fontStyle = (self.FontFamily[0], self.FontSize[0])
        GameTitleLabel = Message(self.InfoFrame, text="GAME - SWIMMING", font=fontStyle, bg=self.__Theme.getBackground1(),
                                 fg=self.__Theme.getForeground1(), width=int(round(650 * (self.sizing.width /1366))))
        GameTitleLabel.place(relx=0, rely=0, width=.6 *self.sizing.width, height=.6*self.sizing.height)

        fontStyle = (self.FontFamily[0], self.FontSize[7])
        episodeInfo = "Press the left, down and up arrows to select the respective option to move faster(the red player).\nClick on the pool to start a race."
        self.GameDescriptionLabel = Message(self.InfoFrame, text=episodeInfo, font=fontStyle,
                                     bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(),
                                       width = int(round(600 * (self.sizing.width / 1366))))
        self.GameDescriptionLabel.place(relx=0, rely=.7, width=.6 * self.sizing.width, height=.2*self.sizing.height)

        moveBackButtonFont = (self.sizing.FontFamily[0], self.sizing.FontSize[5])
        self.MoveBackButton = Button(self.InfoFrame, text="EXIT", bg=self.__Theme.getBackground2(), cursor="hand2",
                                     fg=self.__Theme.getForeground1(), command=lambda: self.ReturnToMenu(),
                                     font=moveBackButtonFont, bd=0, activebackground=self.__Theme.getBackground2())
        self.MoveBackButton.place(relx=.8, rely=.505, height=.8*.15*self.sizing.height, width=.8*.15*self.sizing.width)

        self.PlayGameButton = Button(self.InfoFrame, text="PLAY", bg=self.__Theme.getBackground2(),
                                     fg=self.__Theme.getForeground1(), cursor="hand2",
                                     font=moveBackButtonFont, bd=0, activebackground=self.__Theme.getBackground2())
        self.PlayGameButton.place(relx=.8, rely=.345, height=.8*.15*self.sizing.height, width=.8*.15*self.sizing.width)

        self.InterfaceWindow.bind("<Button-1>", lambda event: self.LoadGame(event))
        self.InterfaceWindow.bind("<Key>", lambda event: self.LoadGame(event))

    def LoadGame(self, event):
        if event.widget == self.PlayGameButton:
            self.GameDescriptionLabel['text'] = "Loading game..."
            self.InterfaceWindow.after(3000, lambda: self.__Load())

    def __Load(self):
        self.ScreenCanvas.destroy()
        SwimmingGame(self.InterfaceWindow, self.sizing, self.user)

    def ReturnToMenu(self):
        from Menu import Main
        # Returns to menu
        Main(self.InterfaceWindow, self.sizing, self.user)

class BoardGameIntro:
    def __init__(self, window, sizings, user):
        #Generates neccsesary attributes
        self.Tasks = []
        self.user = user
        Fonts = [90, 80, 70, 60, 50, 40, 30, 20]
        self.FontFamily = ["Microsoft YaHei UI Light", "Ebrima"]
        self.interfaceDirectory = os.getcwd()
        padding = 80

        self.InterfaceWindow = window

        #Generates neccesary sizings
        sizing = sizings
        self.sizing = sizing
        self.padding = sizing.padding
        self.screenWidth = sizing.width
        self.screenHeight = sizing.height
        self.FontSize = sizing.FontSize
        self.DirectoryHandler = DirectoryHandler()
        self.__Theme = Theme()

        #Ensure canvas is in centre of screen
        self.ScreenCanvas = Frame(self.InterfaceWindow)
        self.ScreenCanvas.place(relx=sizing.canvasPosX, rely=sizing.canvasPosY, width=self.screenWidth,
                                height=self.screenHeight)

        self.DirectoryHandler.changeDirectoryToBackground()
        background = PhotoImage(file="force.png")
        self.DirectoryHandler.changeDirectoryToMain()

        BackgroundLabel = Label(self.ScreenCanvas, image=background)
        BackgroundLabel.place(relx=0, rely=0)

        self.ShowIntro()

        threading.Thread(target=self.InterfaceWindow.mainloop(), args=()).start()

    def ShowIntro(self):
        self.InfoFrame = Frame(self.ScreenCanvas, bg=self.__Theme.getBackground1())
        self.InfoFrame.place(relx=.1, rely=.1, width=.8*self.sizing.width, height=.8*self.sizing.height)

        fontStyle = (self.FontFamily[0], self.FontSize[0])
        GameTitleLabel = Message(self.InfoFrame, text="GAME - THE FORCE", font=fontStyle, bg=self.__Theme.getBackground1(),
                                 fg=self.__Theme.getForeground1(), width=int(round(650 * (self.sizing.width /1366))))
        GameTitleLabel.place(relx=0, rely=0, width=.6 *self.sizing.width, height=.6*self.sizing.height)

        fontStyle = (self.FontFamily[0], self.FontSize[7])
        episodeInfo = "Use your left and right arrows to return to menu/proceed with game. To skip intro press space."
        self.GameDescriptionLabel = Message(self.InfoFrame, text=episodeInfo, font=fontStyle,
                                     bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(),
                                       width = int(round(600 * (self.sizing.width / 1366))))
        self.GameDescriptionLabel.place(relx=0, rely=.7, width=.6 * self.sizing.width, height=.2*self.sizing.height)

        moveBackButtonFont = (self.sizing.FontFamily[0], self.sizing.FontSize[5])
        self.MoveBackButton = Button(self.InfoFrame, text="EXIT", bg=self.__Theme.getBackground2(), cursor="hand2",
                                     fg=self.__Theme.getForeground1(), command=lambda: self.ReturnToMenu(),
                                     font=moveBackButtonFont, bd=0, activebackground=self.__Theme.getBackground2())
        self.MoveBackButton.place(relx=.8, rely=.505, height=.8*.15*self.sizing.height, width=.8*.15*self.sizing.width)

        self.PlayGameButton = Button(self.InfoFrame, text="PLAY", bg=self.__Theme.getBackground2(),
                                     fg=self.__Theme.getForeground1(), cursor="hand2",
                                     font=moveBackButtonFont, bd=0, activebackground=self.__Theme.getBackground2())
        self.PlayGameButton.place(relx=.8, rely=.345, height=.8*.15*self.sizing.height, width=.8*.15*self.sizing.width)

        self.InterfaceWindow.bind("<Button-1>", lambda event: self.startStoryLine(event))
        self.InterfaceWindow.bind("<Key>", lambda event: self.startStoryLine(event))

    def startStoryLine(self, event):
        print(event.keysym)
        if event.keysym == "Left":
            self.ReturnToMenu()
        elif event.keysym == "Right":
            self.GameDescriptionLabel['text'] = "Loading game..."
            self.InterfaceWindow.after(100, lambda: self.createEpisode())
        elif event.keysym.upper() == "X":
            self.ReturnToMenu()

        if event.widget == self.PlayGameButton:
            self.GameDescriptionLabel['text'] = "Loading game..."
            self.InterfaceWindow.after(100, lambda: self.createEpisode())

    def createEpisode(self):
        episodeText1 = "You are in the city of Shenmi. You have been sent on an errand by your father to buy some food from a nearby shop in a busy street."
        episodeText2 = "As you approach the market, you notice a man that steals some apples and run off."
        episodeText3 = "Stop right There"
        episodeText4 = "After him!"
        episodeText5 = "The man runs out the shop with the guards."
        episodeText6 = "You leave the shop. The street is empty."
        episodeText7 = "You then look around to find a dead man on the floor. A door to a shop on the opposite side of the road opens."
        episodeText8 = "HEY! YOU THERE! WHO DO YOU THINK YOU ARE LOOKING AT?!"
        episodeText9 = "You run."
        episodeText10 = "He catches up with you."
        episodeText11 = "You are stopped by another man on the other corner."
        episodeText12 = "Going somewhere?"
        episodeText13 = "Let’s see how tough you are by the time I’m finished with…"
        episodeText14 = "That's where them - the Force"
        episodeText15 = "You became an agent, part of the force"
        episodeText16 = "They took you in and you've undergone lots of lessons"
        episodeText17 = "Now, you must chase your enemy Rival through the grid before they get the stolen treasure"
        episodeText18 = "The treasure is located ahead of a 100 block pathway similar to that of a snake and ladders game"
        episodeText19 = "You and Rival are at this block for either to move they must answer a question correctly"
        episodeText20 = "A machine determines whose turn it is and then the a question is asked to that one"
        episodeText21 = "Once you get a question right a dice will be rolled to determine how far you move forward"
        episodeText22 = "The same will happen for Rival when he is given a chance to go."
        episodeText23 = "For this assigment remember: to diffrentiate you multiply the coefficient by the power"
        episodeText24 = "and reduce the degree by -1"
        episodeText25 = "Integration you do the opposite. You increase the power and divide the coedfficient by that"
        episodeText26 = "Enjoy your mission"

        Slide1 = SlideData("narration", ["market.png", episodeText1, "TC"])
        Slide2 = SlideData("narration", ["market.png", episodeText2, "TC"])
        Slide3 = SlideData("convo", ["market.png", "guard1", episodeText3])
        Slide4 = SlideData("convo", ["market.png", "guard2", episodeText4])
        Slide5 = SlideData("narration", ["street1.png", episodeText5, "TC"])
        Slide6 = SlideData("narration", ["street1.png", episodeText6, "TC"])
        Slide7 = SlideData("narration", ["street1.png", episodeText7, "TC"])
        Slide8 = SlideData("convo", ["street1.png", "villain1", episodeText8])
        Slide9 = SlideData("narration", ["street1.png", episodeText9, "TC"])
        Slide10 = SlideData("narration", ["street1.png", episodeText10, "TC"])
        Slide11 = SlideData("narration", ["street1.png", episodeText11, "TC"])
        Slide12 = SlideData("convo", ["street1.png", "villain2", episodeText12])
        Slide13 = SlideData("convo", ["street1.png", "villain1", episodeText13])
        Slide14 = SlideData("narration", ["force.png", episodeText14, "TC"])
        Slide15 = SlideData("narration", ["force.png", episodeText15, "TC"])
        Slide16 = SlideData("narration", ["force.png", episodeText16, "TC"])
        Slide17 = SlideData("narration", ["questInfo.png", episodeText17, "TC"])
        Slide18 = SlideData("narration", ["questInfo.png", episodeText18, "TC"])
        Slide19 = SlideData("narration", ["questInfo.png", episodeText19, "TC"])
        Slide20 = SlideData("narration", ["questInfo.png", episodeText20, "TC"])
        Slide21 = SlideData("narration", ["questInfo.png", episodeText21, "TC"])
        Slide22 = SlideData("convo", ["calculus.png", "narrator", episodeText22])
        Slide23 = SlideData("convo", ["calculus.png", "narrator", episodeText23])
        Slide24 = SlideData("convo", ["calculus.png", "narrator", episodeText24])
        Slide25 = SlideData("convo", ["calculus.png", "narrator", episodeText25])
        Slide26 = SlideData("convo", ["calculus.png", "narrator", episodeText26])

        slideArray = [Slide2, Slide3, Slide4, Slide5, Slide6, Slide7, Slide8, Slide9, Slide10,
                      Slide11, Slide12, Slide13, Slide14, Slide15, Slide16, Slide17, Slide18,
                      Slide19, Slide20, Slide21, Slide22, Slide23, Slide24, Slide25, Slide26]

        self.Episode = Episode(Slide1, self.InterfaceWindow, self.sizing)

        for slide in slideArray:
            self.Episode.AddSlide(slide, self.InterfaceWindow, self.sizing)

        self.Episode.StartEpisode()

        # self.InterfaceWindow.bind("<space>", lambda event: self.moveToPreviousSlide(event))
        self.InterfaceWindow.bind("<Key>", lambda event: self.moveToNextSlide(event))

    def ReturnToMenu(self):
        from Menu import Main
        # Returns to menu
        Main(self.InterfaceWindow, self.sizing, self.user)

    def moveToNextSlide(self, event):
        try:
            if event.keysym == "Right":
                try:
                    self.Episode.NextSlide()
                except TypeError:
                    BoardGame(self.InterfaceWindow, self.sizing, self.user)

            elif event.keysym == "Left":
                try:
                    self.Episode.PreviousSlide()
                except:
                    self.ReturnToMenu()
            elif event.keysym == "space":
                self.MoveBackButton.destroy()
                BoardGame(self.InterfaceWindow, self.sizing, self.user)
        except TypeError:
            self.MoveBackButton.destroy()
            BoardGame(self.InterfaceWindow, self.sizing, self.user)
