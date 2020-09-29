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

class PromptData:
    def __init__(self, title, Message):
        self.__title = title
        self.__message = Message

    def getTitle(self):
        return self.__title

    def getMessage(self):
        return self.__message

class Prompt:
    def __init__(self, window, sizing, user, text):
        self.__Theme = Theme()

        self.window = window
        self.Fonts = [90, 80, 70, 60, 50, 40, 30, 20]
        self.FontFamily = ["Microsoft YaHei UI Light", "Ebrima", "Courier New"]
        self.interfaceDirectory = os.getcwd()
        self.padding = 80
        self.balls = 5
        self.score = 0
        self.__goAhead = None

        self.gameOver = False

        self.sizing = sizing
        self.user = user

        self.PromptMessage = PromptData(text[0], text[1])

        self.SlideFrame = Frame(self.window, bg=self.__Theme.getBackground1())
        self.SlideFrame.place(relx=self.sizing.canvasPosX + .25, rely=self.sizing.canvasPosY + .25,
                              width=.5 * self.sizing.width1, height=.5 * self.sizing.height1)

        self.__ImplementPrompt(text)

    def __ImplementPrompt(self, text):
        #Collects font styles
        fonstStyleTitle = (self.sizing.FontFamily[0], self.sizing.FontSize[3])
        fonstStyleMessage = (self.sizing.FontFamily[0], self.sizing.FontSize[7])
        fonstStyleButton = (self.sizing.FontFamily[0], self.sizing.FontSize[7], "underline")

        #Widgets for prompts
        PromptDescription = Message(self.SlideFrame, text=self.PromptMessage.getMessage(), font=fonstStyleMessage, bg=self.__Theme.getBackground1(),
                                    fg=self.__Theme.getForeground1(), anchor=W,
                                    width= int(round(500 * (self.sizing.width1 / 1366))) )
        PromptDescription.place(relx=.05, rely=.25, width=.45*self.sizing.width1,
                                height=.275 * self.sizing.height1)

        PromptTitle = Label(self.SlideFrame, text=self.PromptMessage.getTitle(), font=fonstStyleTitle, bg=self.__Theme.getBackground1(),
                            fg=self.__Theme.getForeground1(), anchor=W)
        PromptTitle.place(relx=.05, rely=.05, width=.45*self.sizing.width1)

        ProceedButton = Button(self.SlideFrame, text="Proceed", relief="solid", font=fonstStyleButton,
                               bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(),
                               command= lambda: self.__Proceed(True))
        ProceedButton.config(highlightthickness=1, highlightcolor=self.__Theme.getForeground1(), highlightbackground=self.__Theme.getForeground1())
        ProceedButton.place(relx=(6/16), rely=(6 /9), width= (4/32)*self.sizing.width1,
                          height= .1*self.sizing.height1)

        CancelButton = Button(self.SlideFrame, text="No, Cancel", relief="solid", font=fonstStyleButton,
                               bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(),
                              command=lambda: self.__Close(),highlightthickness=1, highlightcolor=self.__Theme.getForeground1(), highlightbackground=self.__Theme.getForeground1())
        CancelButton.place(relx=(10.8/16), rely=(6 /9), width= (4/32)*self.sizing.width1,
                          height= .1*self.sizing.height1)

    def __Proceed(self, toProceed):
        #Inidicator for interface to carry on with function
        self.__goAhead = toProceed

    def __Close(self):
        self.__goAhead = False
        self.SlideFrame.destroy()

    def getGoAhead(self):
        return self.__goAhead