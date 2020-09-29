import os
orignialDir = os.getcwd()
try:
    os.chdir(os.getcwd() + "\\Tools")
except:
    pass
from Stack import Stack
os.chdir(orignialDir)
import tkinter
import random
from tkinter import *
from sizingAdjust import sizingAdjust
from Theme import Theme
import time
import shutil
import threading
from DirectoryHandler import DirectoryHandler
from Question import Question
import datetime


class Evaluate:
    def __init__(self, window, sizing, user, text, bball=False):
        self.__Theme = Theme()

        self.window = window
        self.Fonts = [90, 80, 70, 60, 50, 40, 30, 20]
        self.FontFamily = ["Microsoft YaHei UI Light", "Ebrima", "Courier New"]
        self.interfaceDirectory = os.getcwd()
        self.padding = 80
        self.balls = 5
        self.score = 0
        self.__ReturnToBasketball = bball
        print(self.__ReturnToBasketball)

        self.gameOver = False

        self.sizing = sizing
        self.user = user

        self.SlideFrame = Canvas(self.window, bg=self.__Theme.getBackground1())
        self.SlideFrame.place(relx=0, rely=0, width=self.sizing.width1,
                              height=self.sizing.height1)

        self.DirectoryHandler = DirectoryHandler()
        self.DirectoryHandler.changeDirectoryToBackground()
        Background = PhotoImage(file="evaluate.png")
        self.DirectoryHandler.changeDirectoryToMain()

        BackgroundLabel = Label(self.SlideFrame, image=Background)
        BackgroundLabel.place(relx=0, rely=0)
        BackgroundLabel.image = Background

        self.__Display(text)

        self.window.bind("<space>", lambda event: self.ReturnToMenu(event))

    def __Display(self, text):
        self.EvaluateFrame = Frame(self.SlideFrame, bg=self.__Theme.getBackground1())
        self.EvaluateFrame.place(relx=.1, rely=.1, width=.8 * self.sizing.width1,
                              height=.8 * self.sizing.height1)

        fontStyle = (self.sizing.FontFamily[0], self.sizing.FontSize[0])
        GameTitleLabel = Message(self.EvaluateFrame, font=fontStyle, bg=self.__Theme.getBackground1(),
                                 fg=self.__Theme.getForeground1(), width=int(round(750 * (self.sizing.width /1366))))
        GameTitleLabel.place(relx=0, rely=.05, width=.7 *self.sizing.width, height=.6*self.sizing.height)

        if self.__ReturnToBasketball == True:
            GameTitleLabel['text'] = "GAME - BASKETBALL GAME"
        else:
            GameTitleLabel['text'] = "GAME - THE\nFORCE"


        fontStyle = (self.sizing.FontFamily[0], self.sizing.FontSize[7])
        self.EvaluateMessage = Message(self.EvaluateFrame, bg="white", font=fontStyle)
        self.EvaluateMessage.place(relx=.675, rely=.0, width=.3 * self.sizing.width1,
                              height=.8 * self.sizing.height1)

        self.EvaluateMessage['text'] = text
    
    def ReturnToMenu(self, event):
        self.SlideFrame.place_forget()
        if self.__ReturnToBasketball == False:
            from Menu import Main
            Main(self.window, self.sizing, self.user)
        elif self.__ReturnToBasketball == True:
            from Menu import Main
            BasketballCourt(self.window, self.sizing, self.user)