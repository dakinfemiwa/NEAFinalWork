import tkinter
import threading
from Tools.DirectoryHandler import DirectoryHandler
from Tools.sizingAdjust import sizingAdjust
from tkinter import *
from tkinter import ttk
from User import User
from DataHandler import DataHandler
from Stack import Stack
import random
from Theme import Theme
from Tree import BinaryTreeArray
from Timer import Timer
from Question import Question
from Tree import Tree
from PIL import ImageTk, Image

import os,sys
import time
from Evaluate import Evaluate

class GameSlide:
    def __init__(self, window, sizing, user):
        self.Theme = Theme()
        self.score = 0
        self.window = window
        self.sizing = sizing
        self.user = user
        self.sizing = sizing

        self.ScreenCanvas = Canvas(self.window, bg=self.Theme.getBackground1())
        self.ScreenCanvas.place(relx=self.sizing.canvasPosX, rely=self.sizing.canvasPosY, width=self.sizing.width,
                              height=self.sizing.height)

        self.DirectoryHandler = DirectoryHandler()
        self.CorrectQuestions = 0


    def evaluate(self, changeInCoin, highScore=None, win=None):


        if win == True:
            text = "You win!\n"
            if self.CorrectQuestions > 0:
                coins = int(round(self.score * .05)) + 50
        elif win == False:
            text = "You lose!\n"
            if self.CorrectQuestions > 0:
                coins = int(round(self.score * .5)) + 50
        elif win == None:
            text = ""
            if self.CorrectQuestions > 0:
                coins = int(round(self.score * .5)) + 50
            elif self.CorrectQuestions == 0:
                coins = 0
        else:
            text = ""
            if self.CorrectQuestions > 0:
                coins = int(round(self.score * .05)) + 50
            else:
                coins = 0


        if highScore != None:
            highScore = self.user.getHighScore()
            self.user.placeScore(self.score)
            HighScore2 = self.user.getHighScore()
            if highScore == None:
                newHighScore = True
            elif HighScore2 > highScore:
                newHighScore = True
            else:
                newHighScore = False

            if newHighScore == True:
                text = text + f"NEW HIGH SCORE!\n"

        if win == True or win == False:
            if self.CorrectQuestions >0:
                coins = int(round(self.CorrectQuestions * .05)) + 50
            else:
                coins = 0
            if win == True:
                coins = 250
            text = text + f"You earned {coins} coins"
        else:
            text = text + f"Your score: {self.score}\nYou earned {coins} coins"

        if highScore != None:
            averageScore = 20

        self.user.changeCoins(changeInCoin)
        if win == None:
            Evaluate(self.window, self.sizing, self.user, text, True)
        else:
            Evaluate(self.window, self.sizing, self.user, text, False)

    #Generates questions of a specific type
    def GenerateQuestion(self, type):
        question = Question(type, True)
        question, correctAnswer, options, correctLane = question.GetQuestion()

        return question, correctAnswer, options, correctLane


class BGMain(GameSlide):
    def __init__(self, window, sizing, user, difficulty):
        super().__init__(window, sizing, user)
        self.__Theme = self.Theme
        self.Fonts = [90, 80, 70, 60, 50, 40, 30, 20]
        self.sizing.FontFamily = ["Microsoft YaHei UI Light", "Ebrima", "Courier New"]
        self.interfaceDirectory = os.getcwd()
        self.padding = 80
        self.balls = 5
        self.score = 0

        self.difficulty = difficulty

        self.gameOver = False

        self.sizing = sizing
        self.user = user

        self.DirectoryHandler.changeDirectoryToBackgroundGameNA()
        photoImage = PhotoImage(file='basketballNet.png')
        self.DirectoryHandler.changeDirectoryToMain()

        bgPosX = int(round(self.sizing.width / 2))
        bgPosY = int(round(self.sizing.height / 2))

        self.Background = self.ScreenCanvas.create_image(bgPosX, bgPosY, image=photoImage)

        textX1 = int(round(self.sizing.width * (5.290 / 32)))
        textX2 = int(round(self.sizing.width * (16.00 / 32)))
        textX3 = int(round(self.sizing.width * (26.71 / 32)))

        textY = int(round(self.sizing.height * (5.80 / 18)))

        fontStyle = (self.sizing.FontFamily[2], self.sizing.FontSize[7])

        self.Option1Text = self.ScreenCanvas.create_text(textX1, textY, text=" - ", fill=self.__Theme.getForeground1(), font=fontStyle)
        self.Option2Text = self.ScreenCanvas.create_text(textX2, textY, text=" - ", fill=self.__Theme.getForeground1(), font=fontStyle)
        self.Option3Text = self.ScreenCanvas.create_text(textX3, textY, text=" - ", fill=self.__Theme.getForeground1(), font=fontStyle)

        self.DirectoryHandler.changeDirectoryToGameProps()
        self.netImage = PhotoImage(file='net.png')


        netPosition1 = int(round(self.sizing.width * (5.35 / 32)))
        netPosition2 = int(round(self.sizing.width * (16.0 / 32)))
        netPosition3 = int(round(self.sizing.width * (26.69 / 32)))
        self.ScreenCanvas.update()

        netHeight = int(round(self.sizing.height * (9.00 / 18)))

        self.netImage1 = self.ScreenCanvas.create_image(netPosition1, netHeight, image=self.netImage)
        self.netImage2 = self.ScreenCanvas.create_image(netPosition2, netHeight, image=self.netImage)
        self.netImage3 = self.ScreenCanvas.create_image(netPosition3, netHeight, image=self.netImage)

        self.basketballHeight = 0.8 * self.sizing.height
        self.basketballWidth = 1.0 * self.sizing.width
        basketballImage = PhotoImage(file="basketball.png")
        self.DirectoryHandler.changeDirectoryToMain()

        self.basketball = self.ScreenCanvas.create_image(self.basketballWidth, self.basketballHeight,
                                                       image=basketballImage)

        self.pressed = False

        self.QuestionBoard = Frame(self.ScreenCanvas, bg=self.__Theme.getBackground1())
        self.QuestionBoard.place(relx=0, rely=0, width=self.sizing.width, height=0.2 * self.sizing.height)

        textWidth = (800 / 1366) * self.sizing.width

        self.QuestionMessage = Message(self.QuestionBoard, width=textWidth,
                                       font=(self.sizing.FontFamily[0], self.sizing.FontSize[7]),
                                       bg=self.__Theme.getBackground1())
        self.QuestionMessage.place(relx=0, rely=0, width=0.7 * self.sizing.width, height=self.sizing.height * .2)

        self.ScreenCanvas.tag_lower(self.Background)

        self.DisplayInfo()

        self.window.bind("<space>", lambda event: self.shoot(event))

        threading.Thread(target=self.play(), args=()).start()
        threading.Thread(target=self.moveBall(), args=()).start()
        threading.Thread(target=self.window.mainloop(), args=()).start()

    def DisplayInfo(self):
        gameInfo = f"Score: {self.score}\nBalls: {self.balls}"

        textWidth = (300 / 1366) * self.sizing.width

        self.GameInfoMessage = Message(self.QuestionBoard, width=800, text=gameInfo, anchor=W,
                                       font=(self.sizing.FontFamily[0], self.sizing.FontSize[7]),
                                       bg=self.__Theme.getBackground1())
        self.GameInfoMessage.place(relx=0.7, rely=0, width=0.3 * self.sizing.width, height=self.sizing.height * .2)

    def UpdateDisplayInfo(self):
        gameInfo = f"Score: {self.score}\nBalls: {self.balls}"
        self.GameInfoMessage['text'] = gameInfo
        #print("Updated")

    def moveBall(self):
        while self.gameOver == False:
            time.sleep(.02)
            if self.pressed == False:
                originalPos = self.basketballWidth
                if self.difficulty == "Easy":
                    self.basketballWidth -= 10
                if self.difficulty == "Medium":
                    self.basketballWidth -= 10
                if self.difficulty == "Hard":
                    self.basketballWidth -= 20

                if self.basketballWidth <= -.05 * self.sizing.width:
                    self.basketballWidth = 1.0 * self.sizing.width
                xChange = self.basketballWidth - originalPos
                self.ScreenCanvas.move(self.basketball, xChange, 0)
                self.ScreenCanvas.update()

    def play(self):
        self.AnsweredQuestion = False
        QuestionStr, self.correctanswer, options, self.correctOption = self.GenerateQuestion("momentum")
        self.option = options
        #print(options)
        self.QuestionMessage['text'] = QuestionStr

        try:
            option1Value = "{:.1f}".format(options[0])
            option2Value = "{:.1f}".format(options[1])
            option3Value = "{:.1f}".format(options[2])
        except:
            option1Value = options[0]
            option2Value = options[1]
            option3Value = options[2]

        self.ScreenCanvas.itemconfig(self.Option1Text, text=option1Value)
        self.ScreenCanvas.itemconfig(self.Option2Text, text=option2Value)
        self.ScreenCanvas.itemconfig(self.Option3Text, text=option3Value)

        return True

    def shoot(self, event):
        self.__accurate, self.option = self.CheckIfOptionSelected()

        self.ShootBall()

        if self.__accurate == True:
            self.ScreenCanvas.tag_raise(self.basketball)
            print(("CORRECT OPTION", self.correctOption))

            correct = self.CheckAnswer(self.option, self.correctOption)
            if correct == True:
                self.score += 3
                threading.Thread(target=self.DisplayMessage("Correct"), args=()).start()
            #Checks if the user shot the ball in the wrong net
            elif correct == False:
                self.balls -= 1
                threading.Thread(target=self.DisplayMessage("Wrong", self.correctOption), args=()).start()

        #If the user missed a shot
        else:
            self.balls -= 1
            threading.Thread(target=self.DisplayMessage("Miss"), args=()).start()

        if self.balls == 0:
            self.gameOver = True
            self.ScreenCanvas.place_forget()
            self.evaluate(int(round(self.score / 10)), True)
        else:
            self.play()

        self.UpdateDisplayInfo()

    def closeMessage(self):

        self.MessageFrame.place_forget()

        self.pressed = False

    def DisplayMessage(self, messageType, correctOption=None):

        self.MessageFrame = Frame(self.ScreenCanvas, bg=self.__Theme.getBackground2(), bd=2)
        self.MessageFrame.place(relx=.25, rely=.25, width=.5 * self.sizing.width,
                                height=.5 * self.sizing.height)

        MessageText = Label(self.MessageFrame,
                            font=(self.sizing.FontFamily[2],
                                  self.sizing.FontSize[5], "bold", "underline"), bg=self.__Theme.getBackground2(),
                            fg=self.__Theme.getForeground1())
        MessageText.place(relx=.05, rely=.05)

        MessageBoxLog = Text(self.MessageFrame, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(),
                             font=(self.sizing.FontFamily[2],
                                   self.sizing.FontSize[5]), bd=0, state=DISABLED)
        MessageBoxLog.place(relx=.05, rely=.3, width=.45 * self.sizing.width, height=.5 * .65 * self.sizing.height)

        if messageType == "Miss":
            MessageText['text'] = "Missed!"
            MessageBoxLog.config(state=NORMAL)
            text = f"Come on! You can do better\nYou have {self.balls} balls."
            MessageBoxLog.insert(END, text)
            MessageBoxLog.config(state=DISABLED)

        elif messageType == "Wrong":
            MessageText['text'] = "Wrong!"
            MessageBoxLog.config(state=NORMAL)
            text = f"The correct answer is {self.correctanswer}.\nYou have {self.balls} balls."
            MessageBoxLog.insert(END, text)
            MessageBoxLog.config(state=DISABLED)

        elif messageType == "Correct":
            MessageText['text'] = "Correct!"
            MessageBoxLog.config(state=NORMAL)
            text = f"You earn 3 points!"
            MessageBoxLog.insert(END, text)
            MessageBoxLog.config(state=DISABLED)

        CloseX = 1 - (((.2 * .5) * self.sizing.height) / (self.sizing.width / 2))

        CloseButton = Button(self.MessageFrame, text="×", bd=0, bg=self.__Theme.getBackground1(),
                             fg=self.__Theme.getForeground1(),
                             font=(self.sizing.FontFamily[1], self.sizing.FontSize[4]),
                             command=lambda: self.closeMessage())
        CloseButton.place(relx=CloseX, rely=.0, width=(.2 * .5) * self.sizing.height,
                          height=(.2 * .5) * self.sizing.height)

        self.MessageFrame.after(3000, lambda: self.wait())

    def wait(self):
        self.MessageFrame.place_forget()

    def CheckIfOptionSelected(self):
        ratio = self.basketballWidth / self.sizing.width
        #print("RATIO:  ", ratio * 32)
        if ratio > (4.88 / 32) and ratio < (5.77 / 32):
            return True, 1
        elif ratio > (15.4 / 32) and ratio < (16.48 / 32):
            return True, 2
        elif ratio >= (27.69 / 33.87) and ratio <= (28.79 / 33.87):
            return True, 3
        else:
            return False, None

    def ShootBall(self):
        velocity = int(round(0.06 * self.sizing.height))
        down = False

        while down == False or (self.basketballHeight <= 0.8 * self.sizing.height):
            time.sleep(.02)
            self.ScreenCanvas.move(self.basketball, 0, -velocity)
            self.basketballHeight -= velocity
            velocity -= int(round(0.002 * self.sizing.height))
            if velocity < 0:
                down = True
                if self.__accurate == True:
                    self.ScreenCanvas.tag_raise(self.netImage1)
                    self.ScreenCanvas.tag_raise(self.netImage2)
                    self.ScreenCanvas.tag_raise(self.netImage3)

            self.ScreenCanvas.update()

    def CheckAnswer(self, userOption, correctOption):
        if userOption == correctOption:
            self.CorrectQuestions += 1
            return True
        else:
            return False

class SwimmingGame(GameSlide):
    def __init__(self, window, sizing, user):
        super().__init__(window, sizing, user)

        self.InterfaceWindow = window
        self.__Theme = self.Theme

        #Gathers neccessary data on sizing
        self.sizing = sizing
        self.padding = self.sizing.padding
        self.screenWidth = self.sizing.width
        self.screenHeight = self.sizing.height

        #Ensures canvas is at the centre of the screen
        self.ScreenCanvas = Frame(self.InterfaceWindow)
        self.ScreenCanvas.place(relx=self.sizing.canvasPosX, rely=self.sizing.canvasPosY, width=self.screenWidth, height=self.screenHeight)

        self.GameOver = True

        #Changes directory to /Images/BackgroundGameNA
        self.DirectoryHandler.changeDirectoryToBackgroundGameNA()
        #Loads up the background image as a PhotoImage
        Background = PhotoImage(file="SwimmingPool.png")
        #Returns directory back to normal
        self.DirectoryHandler.changeDirectoryToMain()

        #Creates label to display background
        BackgroundLabel = Label(self.ScreenCanvas, image=Background )
        #Displays Label
        BackgroundLabel.place(relx=0, rely=0)

        #PlaceHolder for 3 options
        self.OptionsFrame = Canvas(self.ScreenCanvas, bg=self.__Theme.getBackground2())
        self.OptionsFrame.place(relx=.55, rely=.6, width=.5*self.sizing.width, height=.4*self.sizing.height)

        #Creates swimming pool as a canvas
        self.SwimmingCanvas = Canvas(self.ScreenCanvas, bg=self.__Theme.getBackground5(), cursor="hand2")
        self.SwimmingCanvas.place(relx=.15, rely=.0, width=.85*self.screenWidth, height=.65*self.screenHeight)

        #Font style used for the placeholder where questions are asked
        fontStyle = (self.sizing.FontFamily[0], self.sizing.FontSize[7])

        #Placeholder to ask questions
        self.QuestionPlaceHolder = Message(self.ScreenCanvas, bg=self.__Theme.getBackground3(), fg=self.__Theme.getForeground1(), font=fontStyle)
        self.QuestionPlaceHolder.place(relx=.15, rely=.65, width=.45*self.screenWidth, height=.35*self.screenHeight)



        #Placeholder for option 1
        self.Option1PlaceHolder = Label(self.ScreenCanvas, bg=self.__Theme.getBackground2(), fg=self.__Theme.getForeground1(), font=fontStyle)
        self.Option1PlaceHolder.place(relx=.675, rely=.725, width=.05 * self.screenWidth)

        #Placeholder for option 2
        self.Option2PlaceHolder = Label(self.ScreenCanvas, bg=self.__Theme.getBackground2(), fg=self.__Theme.getForeground1(), font=fontStyle)
        self.Option2PlaceHolder.place(relx=.775, rely=.725, width=.05 * self.screenWidth)

        #Placeholder for option 3
        self.Option3PlaceHolder = Label(self.ScreenCanvas, bg=self.__Theme.getBackground2(), fg=self.__Theme.getForeground1(), font=fontStyle)
        self.Option3PlaceHolder.place(relx=.875, rely=.725, width=.05 * self.screenWidth)

        #Attribute to determine what lane the user is in
        self.lane = 1

        #A widget used to indicate where the option of an answer it
        self.Shifter = Message(self.ScreenCanvas, bg=self.__Theme.getBackground7())
        self.Shifter.place(relx=.7, rely=.85, width=.05 * self.screenWidth)

        self.ShowInfo()

        timerPlaceholderFont = (self.sizing.FontFamily[0], self.sizing.FontSize[4])
        self.TimerPlaceHolder = Message(self.ScreenCanvas, bg=self.__Theme.getBackground2(),
                                     fg=self.__Theme.getForeground1(), font=timerPlaceholderFont, bd=0)
        self.TimerPlaceHolder.place(relx=0, rely=.7, width=.15 * self.sizing.width,
                                    height=.15*self.sizing.height)

        moveBackButtonFont = (self.sizing.FontFamily[0], self.sizing.FontSize[4])
        self.MoveBackButton = Button(self.ScreenCanvas, text="☰", bg=self.__Theme.getBackground1(),
                                     fg=self.__Theme.getForeground1(), command=lambda: self.ReturnToMenu(),
                                     font=moveBackButtonFont, bd=0, activebackground=self.__Theme.getBackground2())
        self.MoveBackButton.place(relx=0, rely=.85, height=.15*self.sizing.height, width=.15*self.sizing.width)

        #Generates a diffrentiation question for the user


        #Binds window so user can go back/play the game
        self.SwimmingCanvas.bind("<Button-1>", lambda event: self.StartGame(event))
        self.InterfaceWindow.bind("<Key>", lambda event: self.GoBack(event))

        threading.Thread(target=self.InterfaceWindow.mainloop(), args=()).start()

    def ShowInfo(self):
        fontStyle = (self.sizing.FontFamily[0], self.sizing.FontSize[3])
        Textx = self.screenWidth * .85 * 0.5
        Texty = self.screenHeight * .65 * 0.5
        self.PlayText = self.SwimmingCanvas.create_text(Textx, Texty, text="Click to play", font=fontStyle,
                                                        fill=self.__Theme.getBackground1())

        fontStyle = (self.sizing.FontFamily[0], self.sizing.FontSize[7])
        self.TipFrame = Message(self.ScreenCanvas, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(),
                                font=fontStyle, width=(150* (self.sizing.width / 1366)))
        self.TipFrame.place(relx=0, rely=0, height=.55*self.sizing.height, width=.15*self.sizing.width)

        DifficultyFrame = Frame(self.ScreenCanvas, bg=self.__Theme.getBackground1())
        DifficultyFrame.place(relx=0, rely=.5, height=.2*self.sizing.height, width=.15*self.sizing.width)

        self.Difficulties = ["Easy", "Medium", "Hard", "Insane"]

        self.DifficultyIndex = 0
        self.Difficulty = self.Difficulties[self.DifficultyIndex]

        navigationFontStyle = (self.sizing.FontFamily[0], self.sizing.FontSize[7])
        UpButton = Button(DifficultyFrame, text="▲", bd=0, bg=self.__Theme.getBackground1(),
                          fg=self.__Theme.getForeground1(), font=navigationFontStyle,
                          activebackground=self.__Theme.getBackground1(), cursor="hand2",
                          command=lambda: self.changeDifficulty("-")  )
        UpButton.place(relx=0, rely=.1, width=.15*self.sizing.width)

        self.DifficultyPlaceHolder = Message(DifficultyFrame, text=self.Difficulty, font=fontStyle, justify="center",
                                           bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(),
                                            anchor=CENTER)
        self.DifficultyPlaceHolder.place(relx=0, rely=.4, width=.15*self.sizing.width)

        DownButton = Button(DifficultyFrame, text="▼", bd=0, background=self.__Theme.getBackground1(),
                          font=navigationFontStyle, activebackground=self.__Theme.getBackground1(),
                          command=lambda: self.changeDifficulty("+"), cursor="hand2")
        DownButton.place(relx=0, rely=.7, width=.15*self.sizing.width)

        self.GameOver = True

        TipText = "Left for leftermost option, right for rightermost, Down for middle."
        self.TipFrame['text'] = TipText

    def changeDifficulty(self, Direction):
        if self.GameOver == True:
            if Direction == "-":
                self.DifficultyIndex -= 1
            elif Direction == "+":
                self.DifficultyIndex += 1

            if self.DifficultyIndex < 0:
                self.DifficultyIndex = len(self.Difficulties) - 1
            if self.DifficultyIndex > len(self.Difficulties) - 1:
                self.DifficultyIndex = 0

            self.Difficulty = self.Difficulties[self.DifficultyIndex]
            self.DifficultyPlaceHolder['text'] = self.Difficulty
        else:
            return

    def ReturnToMenu(self):
        from Menu import Main
        # Returns to menu
        Main(self.InterfaceWindow, self.sizing, self.user)

    def GoBack(self, event):
        #Checks if the button X is being pressed
        if event.keysym.upper() == "X":
            #Imports module for Menu
            from Menu import Main
            #Returns to menu
            Main(self.InterfaceWindow, self.sizing, self.user)

    #Starts the game
    def StartGame(self, event):
        self.SwimmingCanvas.delete(self.PlayText)

        self.lines = []

        self.GameOver = False

        nodeCount = 9
        self.PhotoImages = []

        for node in range(nodeCount):
            nodeC = (node % 3) + 1
            self.DirectoryHandler.changeDirectoryToGameProps()
            BgPhoto = PhotoImage(file=f"swimmer1.png")
            self.DirectoryHandler.changeDirectoryToMain()
            self.PhotoImages.append(BgPhoto)

        self.DirectoryHandler.changeDirectoryToGameProps()
        self.PlayerSprite = PhotoImage(file="swimmer1Player.png")
        self.DirectoryHandler.changeDirectoryToMain()

        #If the swimming pool was clicked
        if event.widget == self.SwimmingCanvas:
            #Creates array for all players involved
            self.Rivals = []
            #Creates 9 rivals and places them in the swimming pool
            for node in range(nodeCount):
                nodeSize = round( (1 / 30) * self.screenHeight)
                x1 = (.8 * .0) * self.screenWidth + (.025 * self.screenWidth)
                x2 = x1 + nodeSize
                y1 = ((.8 * (node / 12)) * self.screenHeight) + 30
                y2 = y1 + nodeSize


                yLine = (( y1 + (((.8 * ( (node + 1) / 12)) * self.screenHeight) + 30) ) / 2) - 5

                x1Line = 0
                x2Line = .85 * self.screenWidth

                if node != 3:
                    nodeImage = self.SwimmingCanvas.create_image(x1, y1, image=self.PhotoImages[node], tags="image")
                else:
                    nodeImage = self.SwimmingCanvas.create_image(x1, y1, image=self.PlayerSprite, tags="image")

                self.SwimmingCanvas.update()
                #nodeImage = newNode.swimmerNode
                nodeArray = [nodeImage, x2]

                line = self.SwimmingCanvas.create_line(x1Line, yLine, x2Line, yLine, fill=self.__Theme.getLineColour(),
                                                width="3")

                self.lines.append(line)

                #self.SwimmingCanvas.update()
                #Sets specific data relating to each node (node, position)

                self.SpriteIndex = 1


                #Updates it to array
                self.Rivals.append(nodeArray)

                #Updates Canvas
                #self.SwimmingCanvas.update()

                self.DirectoryHandler.changeDirectoryToGameProps()
                self.PhotoImagesSprite = [PhotoImage(file="swimmer1.png"), PhotoImage(file="swimmer2.png"),
                                          PhotoImage(file="swimmer3.png"), PhotoImage(file="swimmer4.png")]
                self.PhotoImagesSpritePlayer = [PhotoImage(file="swimmer1Player.png"), PhotoImage(file="swimmer2Player.png"),
                                          PhotoImage(file="swimmer3Player.png"), PhotoImage(file="swimmer4Player.png")]
                self.DirectoryHandler.changeDirectoryToMain()
            self.InterfaceWindow.bind("<Key>", lambda event: self.MoveSlider(event))

            threading.Thread(target=self.ChangeSpriteImg(), args=()).start()
            threading.Thread(target=self.Play(), args=()).start()

    def ChangeSpriteImg(self):
        if self.GameOver == False:
            for node in self.Rivals:
                index = self.Rivals.index(node)
                self.SwimmingCanvas.delete(node[0])

                self.SpriteIndex += 1
                self.SpriteIndex %= 4

                y1 = ((.8 * (index / 12)) * self.screenHeight) + 30

                if index != 3:
                    nodeImage = self.SwimmingCanvas.create_image(node[1], y1, image=self.PhotoImagesSprite[self.SpriteIndex],
                                                             tags="image")
                else:
                    pass
                    nodeImage = self.SwimmingCanvas.create_image(node[1], y1, image=self.PhotoImagesSpritePlayer[self.SpriteIndex],
                                                             tags="image")

                node[0] = nodeImage
        else:
            return

        self.InterfaceWindow.after(100, lambda: self.ChangeSpriteImg())

    def updateTimer(self):
        time = self.timer.GetTime()
        self.TimerPlaceHolder['text'] = time
        self.TimerPlaceHolder.after(100, lambda: self.updateTimer())

    def Play(self):
        self.GenerateQuestionInterface()
        self.GameOver = False

        if self.Difficulty == "Easy":
            lowerBound = 1
            upperBound = 3
        elif self.Difficulty == "Medium":
            lowerBound = 2
            upperBound = 4
        elif self.Difficulty == "Hard":
            lowerBound = 4
            upperBound = 6
        elif self.Difficulty == "Insane":
            lowerBound = 6
            upperBound = 8

        #Indicator which ranks all players
        self.rank = 1
        #Boolean for if the race is over
        breakable = False

        self.__Move(upperBound, lowerBound)

        self.timer = Timer()
        threading.Thread(target=self.timer.StartTimer(self.ScreenCanvas), args=()).start()
        threading.Thread(target=self.updateTimer(), args=()).start()

    def __Move(self, upperBound, lowerBound):
        breakable = False
        go = 0
        threading.Thread(target=self.checkLane(), args=()).start()

        for node in self.Rivals:
            index = self.Rivals.index(node)
            if node[1] < .825 * self.screenWidth:
                #Randomly generates how fast they move each time
                movement = random.randint(lowerBound, upperBound)
                movement /= 2

                if index == 3:
                    movement /=1.1

                try:
                    #self.SwimmingCanvas.move(node[0], movement, 0)
                    node[1] += movement
                    node[0] = newNode
                except:
                    pass

            #Refreshes canvas
            "self.SwimmingCanvas.update()"
            #If node is at the end of the race
            if node[1] >= .825 * self.screenWidth and len(node) == 2:
                #Give it a rank
                node.append(self.rank)
                node.append(self.timer.GetTime())
                #Add the rank variable for next node that finishes race
                self.rank += 1

            print((self.rank, len(self.Rivals) + 1))

            #If race is over
            if self.rank > len(self.Rivals):
                #Sets boolean to True thus finishing the race
                breakable = True

        if breakable == True:
            self.GameOver = True
            self.timer.StopTimer()
            self.Evaluate()
        else:
            self.InterfaceWindow.after(95, lambda: self.__Move(upperBound, lowerBound))


    def MoveSlider(self, event):
        if len(self.Rivals[3]) == 2:
            #Checks if the left keypad was pressed
            if event.keysym == "Left":
                #If so it moves the slider to the left
                #If at the leftermost
                self.lane = 1
            #Checks if the right keypad was pressed
            elif event.keysym == "Right":
                #If so it moves the slider to the right
                #Slider is moved to lane 3
                self.lane = 3

            elif event.keysym == "Down":
                #If so it moves the slider to the middle
                self.lane = 2

            #Positions the slider according to its new lane
            if self.lane == 1:
                self.Shifter.place(relx=.675, rely=.875, width=.05 * self.screenWidth)
            elif self.lane == 2:
                self.Shifter.place(relx=.775, rely=.875, width=.05 * self.screenWidth)
            elif self.lane == 3:
                self.Shifter.place(relx=.875, rely=.875, width=.05 * self.screenWidth)
        else:
            self.QuestionPlaceHolder['text'] = "You finished the race!"
            self.Option1PlaceHolder['text'] = "N/A"
            self.Option2PlaceHolder['text'] = "N/A"
            self.Option3PlaceHolder['text'] = "N/A"

    def ConvertToString(self, coefficient, degree):
        #Adds the power to the polynomial experssions
        string = str(coefficient) + "x"
        if degree == 2:
            string += "²"
        elif degree == 3:
            string += "³"
        elif degree == 4:
            string += "⁴"
        elif degree == 5:
            string += "⁵"
        elif degree == 6:
            string += "⁶"
        elif degree == 7:
            string += "⁷"
        elif degree == 8:
            string += "⁸"
        elif degree == 0:
            string = str(coefficient)

        return string


    def  GenerateQuestionInterface(self):
        self.lane = 0
        self.Shifter.place_forget()
        topics = ["speed", "projectile"]
        random.shuffle(topics)

        QuestionString, self.correctanswer, options, self.correctOption = self.GenerateQuestion(topics[0])

        #Updates placeholders
        self.QuestionPlaceHolder['text'] = QuestionString
        self.Option1PlaceHolder['text'] = options[0]
        self.Option2PlaceHolder['text'] = options[1]
        self.Option3PlaceHolder['text'] = options[2]

    #Checks if the slider is on the lane representing the correct answer
    def checkLane(self):
        if self.GameOver == False:
            #If so
            if self.lane == self.correctOption:
                self.CorrectQuestions += 1
                #Another question can be genreated
                self.GenerateQuestionInterface()
                #Checks if the node is at the end of the race
                if self.Rivals[3][1] < (.825 * self.screenWidth):
                    #If not it moves user's node
                    self.SwimmingCanvas.move(self.Rivals[3][0], 20, 0)
                    self.Rivals[3][1] += 20
                    #Update canvas
                    self.SwimmingCanvas.update()
                else:
                    if len(self.Rivals[3]) == 2:
                        #Gives it a rank if at the end of the range
                        self.Rivals[3].append(self.rank)
                        self.Rivals[3].append(self.timer.GetTime())
                        self.rank += 1
                    return
            else:
                pass

    def Evaluate(self):
        fastestTimeBefore = self.user.getFastestSwimingTime()
        time = float(self.Rivals[3][3])
        self.user.addSwimmingTime(time)
        fastestTimeNow = self.user.getFastestSwimingTime()

        if fastestTimeBefore != None:
            if fastestTimeBefore > fastestTimeNow:
                personalBest = True
            else:
                personalBest = False
        else:
            personalBest = False

        #issues report of race
        self.CommentsFrame = Canvas(self.SwimmingCanvas, bg=self.__Theme.getBackground5())
        self.CommentsFrame.place(relx=0,rely=0, width=.85*self.screenWidth, height=.65*self.screenHeight)

        #Placeholder for comments
        fontStyle = (self.sizing.FontFamily[1], int(round (self.sizing.FontSize[7] * 0.75) ) )
        self.CommentLabel = Label(self.CommentsFrame, bg=self.__Theme.getBackground5(), fg=self.__Theme.getBackground1(), font=fontStyle)
        self.CommentLabel.place(relx=.2, rely=.2)

        rankingText = ""
        #Organised list according to rankings
        binaryTreeRanking = BinaryTreeArray(self.Rivals, 2)
        binaryTreeList = binaryTreeRanking.Traverse()
        #print(binaryTreeList)
        #print(self.Rivals)

        pNo = 1
        for player in binaryTreeList:
            if player == self.Rivals[3]:
                playerName =  "You     "
            else:
                playerName = f"Player {pNo}"
                pNo += 1

            rankingText = rankingText + f"{player[2]}\t{playerName}\t\t\t\t\t{player[3]}"
            rankingText = rankingText + "\n"

        #print(rankingText)

        self.CommentLabel['text'] = rankingText

        self.SwimmingCanvas.after(6500, lambda: self.Comment(personalBest))


    def Comment(self, personalBest):
        self.CommentLabel.place_forget()

        #Placeholder for comments
        fontStyle = (self.sizing.FontFamily[0], self.sizing.FontSize[5])
        self.CommentLabel = Message(self.CommentsFrame, bg=self.__Theme.getBackground5(),
                                    fg=self.__Theme.getForeground1(), font=fontStyle,
                                    width = int(round(600 * (self.sizing.width / 1366))))
        self.CommentLabel.place(relx=.0, rely=.0, width=.8*self.screenWidth, height=.5*self.screenHeight)


        #Checks if the user won
        if len(self.Rivals[3]) ==4:
            if self.Rivals[3][2] == 1:
                #Displays that the user had won
                coins = 250 + int(round(self.CorrectQuestions * 0.5))
                commentTest = f"You won!\nYou earned {coins} coins"
                if personalBest == True:
                    commentTest = commentTest + "\nNew Personanl Best"
                self.CommentLabel['text'] = commentTest
                #Increases the number of coins
                commentTest = commentTest + f"\n You earned {coins} coins"
                self.user.changeCoins(coins)

            #If the user didn't win
            else:
                commentTest = "You didn't quite get it. All the best next time."
                #print(self.Rivals[3][2])
                if self.CorrectQuestions > 0:
                    coins = 50 + int(round(self.CorrectQuestions * 0.5))
                    commentTest = commentTest + f"\n You earned {coins} coins"
                    self.user.changeCoins(50)
                else:
                    coins = 0
                    commentTest = commentTest + f"\n You earned {coins} coins"

                if personalBest == True:
                    commentTest = commentTest + "\nNew Personanl Best"

                #Displays output
                self.CommentLabel['text'] = commentTest

        # If the user didn't win
        else:
            # Displays output
            commentTest = "You didn't quite get it. All the best next time."
            if self.CorrectQuestions > 0:
                coins = 50 + int(round(self.CorrectQuestions * 0.5))
                self.user.changeCoins(coins)
                commentTest = commentTest + f"\n You earned {coins} coins"
            else:
                coins = 0
                commentTest = commentTest + f"\n You earned {coins} coins"

            if personalBest == True:
                commentTest = commentTest + "\nNew Personanl Best"

            self.CommentLabel['text'] = commentTest


        self.InterfaceWindow.after(3500, lambda: self.RestartGame())

    def RestartGame(self):
        #Option for user to restart game
        self.CommentsFrame.place_forget()
        for node in self.Rivals:
            i = self.Rivals.index(node)
            self.SwimmingCanvas.delete(node[0])
            self.SwimmingCanvas.delete(self.lines[i])

        self.GameOver = True

        fontStyle = (self.sizing.FontFamily[0], self.sizing.FontSize[3])
        Textx = self.screenWidth * .85 * 0.5
        Texty = self.screenHeight * .65 * 0.5
        self.PlayText = self.SwimmingCanvas.create_text(Textx, Texty, text="Click to play", font=fontStyle,
                                                        fill=self.__Theme.getBackground1())

        self.SwimmingCanvas.bind("<Button-1>", lambda event: self.StartGame(event))
        
class BoardGame(GameSlide):
    def __init__(self, window, sizing, user):
        super().__init__(window, sizing, user)
        #Generates neccsesary attributes
        self.Tasks = []
        padding = 80

        self.__Theme = Theme()
        self.InterfaceWindow = window

        self.padding = self.sizing.padding
        self.screenWidth = self.sizing.width
        self.screenHeight = self.sizing.height

        self.ScreenCanvas = Frame(self.InterfaceWindow)
        self.ScreenCanvas.place(relx=self.sizing.canvasPosX, rely=self.sizing.canvasPosY, width=self.screenWidth,
                                height=self.screenHeight)

        self.DirectoryHandler.changeDirectoryToBackgroundGameNA()
        Background = PhotoImage(file="quest.png")
        self.DirectoryHandler.changeDirectoryToMain()

        BackgroundLabel = Label(self.ScreenCanvas, image=Background)
        BackgroundLabel.place(relx=0, rely=0, width=self.screenWidth, height=self.screenHeight)

        self.GameCanvas = Frame(self.ScreenCanvas, bg=self.__Theme.getBackground1())
        self.GameCanvas.place(relx=.05, rely=.05, width=.9*self.screenWidth, height=.9*self.screenHeight)

        #Frame where the grid will be drawn
        self.GridFrame = Frame(self.GameCanvas, bg=self.__Theme.getBackground1())
        self.GridFrame.place(relx=0, rely=0, width=.45*self.screenWidth, height=.9*self.screenHeight)

        self.QuestionFrame = Frame(self.GameCanvas, bg=self.__Theme.getBackground2())
        self.QuestionFrame.place(relx=.5, rely=0, width=.45 * self.screenWidth, height=.9 * self.screenHeight)

        fontStyle = (self.sizing.FontFamily[0], self.sizing.FontSize[5])
        self.StatusPlaceHolder = Message(self.QuestionFrame, bg=self.__Theme.getBackground2(), fg=self.__Theme.getForeground1(), font=fontStyle,
                                       text="[Status Title]", width=int( round(400 * (self.screenWidth / 1366))))
        self.StatusPlaceHolder.place(relx=.1, rely=.05)

        fontStyle1 = (self.sizing.FontFamily[0], self.sizing.FontSize[7], "italic")
        self.StatusDescriptionPlaceHolder = Label(self.QuestionFrame, text="[Status Description]", bg=self.__Theme.getBackground2(),
                                                  fg=self.__Theme.getForeground1(), font=fontStyle1)
        self.StatusDescriptionPlaceHolder.place(relx=.1, rely=.3)

        self.DicePlaceHolder = Label(self.QuestionFrame, bg=self.__Theme.getBackground2())
        self.DicePlaceHolder.place(relx=.1, rely=.4, width=self.screenWidth*.45*.8, height=.3*self.screenHeight)

        self.StartGame()

        self.InterfaceWindow.bind("<Key>", lambda: self.blankMethod())
        self.InterfaceWindow.bind("<Return>", lambda: self.blankMethod())
        threading.Thread(target=self.InterfaceWindow.mainloop(), args=()).start()

    def StartGame(self):
        # Creates attributes for the positions of the player and the computer
        self.ComputerPos = 0
        self.PlayerPos = 0

        # Creates attribute for all the questions the user has gotten right
        self.CorrectQuestions = 0

        # Creates string values for
        self.PlayerStr = "PLY"
        self.ComputerStr = "CTR"
        self.Players = [self.ComputerStr, self.PlayerStr]

        # Creates a fresh board
        self.DrawBoard()
        # Plays the game
        self.PrintBoard()

        threading.Thread(target=self.Play(), args=()).start()

    def DrawBoard(self):
        # Creates attribute for array
        self.Board = []
        # Sets the dimensions of the board to a 10x10 grid
        self.dimensions = 10
        for row in range(self.dimensions):
            # add Row
            self.Board.append([])
            for column in range(self.dimensions):
                if row % 2 == 0:
                    no = (row * 10) + (column + 1)
                else:
                    no = (row * 10) + (10 - (column))

                no = 101 - no

                no = self.GetNoAsString(no)

                self.Board[row].append(no)

    def GetNoAsString(self, no):
        if no < 100 and no > 9:
            no = "0" + str(no)
        elif no < 10:
            no = "00" + str(no)
        else:
            no = str(no)

        return no

    def RollDice(self):

        # Informs user to roll dice"
        self.StatusDescriptionPlaceHolder["text"] = "Rolling Dice..."

        self.ScreenCanvas.after(3000, lambda: self.__DisplayResult())

    def __DisplayResult(self):
        ''' Variable to "roll a dice" - generates a random number from 1 to 6
        inclusively.'''
        no = ['One', 'Two','Three', 'Four', 'Five', 'Six']
        # Generates a dice number randomly from 1 to 6
        for roll in range(3):
            self.DiceNumber = random.randint(1, 6)
            # Outputs number rolled
            self.InterfaceWindow.after(1250, lambda: self.shiftDice(no))
        self.Result()

    def shiftDice(self, no):
            self.StatusDescriptionPlaceHolder["text"] = "Number rolled on"
            self.DirectoryHandler.changeDirectoryToDice()
            DiceImage = PhotoImage(file="Dice" + no[self.DiceNumber - 1] + ".png")
            self.DirectoryHandler.changeDirectoryToMain()

            self.DicePlaceHolder.config(image=DiceImage)
            self.DicePlaceHolder.image = DiceImage

    def Result(self):
        if self.turn == "PLY":
            self.PlayerPos += self.DiceNumber
        elif self.turn == "CTR":
            #print("updatingCPos")
            self.ComputerPos += self.DiceNumber

        self.InterfaceWindow.after(3750, lambda: self.NextTurn())

    def ConvertToString(self, coefficient, degree):
        #
        string = str(coefficient) + "x"
        if degree == 2:
            string += "²"
        elif degree == 3:
            string += "³"
        elif degree == 4:
            string += "⁴"
        elif degree == 5:
            string += "⁵"
        elif degree == 6:
            string += "⁶"
        elif degree == 7:
            string += "⁷"
        elif degree == 8:
            string += "⁸"
        elif degree == 0:
            string = str(coefficient)

        return string

    def GenerateQuestion(self):
        topics = ["integration", "diffrentiation"]
        random.shuffle(topics)
        question = Question(topics[0], False)
        QuestionStr, correctAnswer = question.GetQuestion()

        self.QuestionWindow = Frame(self.InterfaceWindow, bg=self.__Theme.getBackground2())
        self.QuestionWindow.place(relx=.1, rely=.25, width=.3*self.screenWidth, height=.5*self.screenHeight)

        fontStyle = (self.sizing.FontFamily[0], self.sizing.FontSize[7])

        self.QuestionPlaceHolder = Message(self.QuestionWindow, width= round(int(295*(self.screenWidth / 1366))),
                                           bg=self.__Theme.getBackground2(),font=fontStyle)
        self.QuestionPlaceHolder.place(relx=.05, rely=.05)

        fontStyle = (self.sizing.FontFamily[1], self.sizing.FontSize[6])

        self.Answer = correctAnswer

        self.QuestionPlaceHolder['text'] = QuestionStr + "\n\nAnswer in the form ax^n(+c where neccessary)"

        self.UserEntry = Entry(self.QuestionWindow, font=fontStyle, bd=0, bg=self.__Theme.getBackground2())
        self.UserEntry.place(relx=.05, rely=.75,width=.25*self.screenWidth)
        self.UserEntry.focus()

        self.UserEntry.bind("<Return>", lambda event: self.CheckAnswer(event, self.UserEntry.get()))

    def NextTurn(self):
        'Starts another round for players'
        self.GridFrame.destroy()

        self.StatusPlaceHolder['text'] = ""
        self.StatusDescriptionPlaceHolder['text'] = ""

        self.GridFrame = Frame(self.GameCanvas, bg=self.__Theme.getBackground1())
        self.GridFrame.place(relx=0, rely=0, width=.45*self.screenWidth, height=.9*self.screenHeight)

        del self.DicePlaceHolder
        self.DicePlaceHolder = Label(self.QuestionFrame, bg=self.__Theme.getBackground2())
        self.DicePlaceHolder.place(relx=.1, rely=.4, width=self.screenWidth*.45*.8, height=.3*self.screenHeight)

        self.PrintBoard()

        if self.ComputerPos >= 100 or self.PlayerPos >= 100:
            if self.PlayerPos >= 100:
                self.evaluate(150, None, win=True)
                return
            elif self.ComputerPos >= 100 and self.CorrectQuestions > 0:
                self.evaluate(50, None, win=False)
                return
            elif self.ComputerPos >= 100 and self.CorrectQuestions == 0:
                self.evaluate(0, None, win=False)
                return
        else:
            pass

        self.Play()

    def CheckAnswer(self, event, userEntry):
        '''Checks if the user's answer is correct'''
        self.QuestionWindow.destroy()
        if userEntry == self.Answer:
            self.StatusPlaceHolder['text'] = "CORRECT!"
            self.CorrectQuestions += 1
            self.InterfaceWindow.after(4000, lambda: self.blankMethod())

            self.StatusDescriptionPlaceHolder['text'] = "Rolling Dice"
            self.InterfaceWindow.after(2000, lambda: self.RollDice())
            self.Correct = True

        else:
            self.StatusPlaceHolder['text'] = "WRONG"
            self.StatusDescriptionPlaceHolder['text'] = f"The correct answer is {self.Answer}"

            self.InterfaceWindow.after(1550, lambda: self.NextTurn())

    def MovePos(self, player):
        '''Changes the value stored for the position of the players as they
        get closer to the trophy'''
        # Checks if the
        if player == "C":
            self.ComputerPos += self.DiceNumber
        else:
            self.PlayerPos += self.DiceNumber

    def ComputerGetsAGo(self):
        '''Method that determines whether the computer will miss a go or
        get a go.'''
        #print("EYEY")
        self.WhetherItGetsAGo = [True, False, True, True]
        self.ComputerGetsAGoYN = self.WhetherItGetsAGo[random.randint(0, 3)]

    #Displays board
    def PrintBoard(self):
        for row in self.Board:
            rowIndex = self.Board.index(row)
            for rowItem in row:
                columnIndex = row.index(rowItem)

                if rowIndex % 2 == 0:
                    no = (rowIndex * 10) + (columnIndex + 1)
                else:
                    no = (rowIndex * 10) + (10 - (columnIndex))

                no = 101 - no

                fontStyle = (self.sizing.FontFamily[0], int(round(self.sizing.FontSize[7] * .8)) )
                RowMessage = Message(self.GridFrame, bg=self.__Theme.getBackground1(), text=no, fg=self.__Theme.getForeground1(), font=fontStyle,
                                     borderwidth = 0, highlightthickness=0)
                RowMessage.place(relx=(1/len(row)*columnIndex), rely=(1/len(self.Board))*rowIndex,
                                 width= (1/ len(row))*.45* self.screenWidth,
                                 height= (1/ len(self.Board)) * .9 * self.screenHeight)

                if no == self.PlayerPos:
                    RowMessage.config(bg=self.__Theme.getBackground5(), fg=self.__Theme.getBackground1())
                elif no == self.ComputerPos:
                    RowMessage.config(bg=self.__Theme.getBackground6(), fg=self.__Theme.getBackground1())

    #Game for the round
    def Play(self):
        if self.ComputerPos >= 100 or self.PlayerPos >=100:
            self.evaluate()

        #print(self.ComputerPos)
        self.goes = random.randint(1, 7)
        random.shuffle(self.Players)

        self.StatusPlaceHolder['text'] = "Deciding whose turn it is..."

        self.InterfaceWindow.after(1000, lambda: self.Play1())

    def Play1(self):
        self.turn = "CTR"
        #self.PlayerBoard = self.Board

        if self.goes % 2 == 0:
            self.turn = self.Players[0]
        else:
            self.turn = self.Players[1]

        if self.turn == "PLY":
            self.StatusPlaceHolder['text'] = "YOUR TURN"
            self.StatusDescriptionPlaceHolder['text'] = "Answer Question"

            self.GenerateQuestion()

        elif self.turn == "CTR":
            self.StatusPlaceHolder['text'] = "RIVAL GETS A QUESTION"
            self.InterfaceWindow.after(4000, lambda: self.RunComputerGo())


    def RunComputerGo(self):
        self.ComputerGetsAGo()

        if self.ComputerGetsAGoYN == True:
            self.StatusPlaceHolder['text'] = "RIVAL GETS IT RIGHT"
            self.RollDice()
        else:
            self.StatusPlaceHolder['text'] = "RIVAL GETS IT WRONG"
            self.InterfaceWindow.after(3500, lambda: self.NextTurn())

    def blankMethod(self):
       pass

    def decidingMethod(self):
        self.StatusPlaceHolder['text'] = "Deciding whose turn it is..."
