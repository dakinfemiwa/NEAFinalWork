import os
orignialDir = os.getcwd()
try:
    os.chdir(os.getcwd() + "\\Tools")
except:
    pass
from Stack import Stack
os.chdir(orignialDir)
# Importing required modules
import tkinter
from tkinter import ttk
from tkinter import *
from DirectoryHandler import DirectoryHandler
from sizingAdjust import sizingAdjust
import threading
from Theme import Theme
from Stack import Stack
import random
import time

class SlideData:
    def __init__(self, type, data=[]):
        self.__SlideType = type

        if self.__SlideType == "convo":
            self.__SlideBackground = data[0]
            self.__SlideCharacter = data[1]
            self.__SlideText = data[2]

        elif self.__SlideType == "narration":
            self.__SlideBackground = data[0]
            self.__SlideText =  data[1]
            self.__SlidePos = data[2]

        else:
            self.__Game = data

    def getSlideBackground(self):
        return self.__SlideBackground

    def getSlideText(self):
        return self.__SlideText

    def getSlideType(self):
        return self.__SlideType

    def getSlidePos(self):
        return self.__SlidePos

    def getSlideCharacter(self):
        return self.__SlideCharacter

    def getGameFunction(self):
        return data

class Episode:
    def __init__(self, firstSlide, window, sizing):
        self.__SlidesReverse = Stack([])
        self.AddSlide(firstSlide, window, sizing)

    def AddSlide(self, SlideParameter, window, sizing):
        from Slide import Convo
        from Slide import Narration
        if SlideParameter.getSlideType() == "narration":
            slide = Narration(window, sizing, SlideParameter.getSlideBackground(), SlideParameter.getSlideText(), SlideParameter.getSlidePos())
        elif SlideParameter.getSlideType() == "convo":
            slide = Convo(window, sizing, SlideParameter.getSlideBackground(), SlideParameter.getSlideText(), SlideParameter.getSlideCharacter())
        else:
            chosenClass = SlideParameter.getGameFunction()
            slide = chosenClass()

        self.__SlidesReverse.Push(slide)

    def __ReverseOrder(self):
        self.__SlidesOrder = Stack([])
        self.__Reverse()

    def __Reverse(self):
        try:
            slide, index = self.__SlidesReverse.Peek()
            self.__SlidesOrder.Push(slide)
            self.__SlidesReverse.Pop()
            if index == 0:
                return
            else:
                self.__Reverse()
        except:
           return

    def StartEpisode(self):
        self.__ReverseOrder()
        slide1, index = self.__SlidesOrder.Peek()
        self.__ViewSlide(slide1)
        
    def NextSlide(self):
        slide, index = self.__SlidesOrder.Peek()
        #slide.SlideFrame.place_forget()
        self.__SlidesOrder.Pop()
        self.__SlidesReverse.Push(slide)
        slide, index = self.__SlidesOrder.Peek()
        self.__ViewSlide(slide)

    def PreviousSlide(self):
        slide, index = self.__SlidesOrder.Peek()
        slide.SlideFrame.place_forget()

        slide, index = self.__SlidesReverse.Peek()
        self.__SlidesReverse.Pop()
        self.__SlidesOrder.Push(slide)
        self.__ViewSlide(slide)

    def __ViewSlide(self, slide):
        slide.viewSlide()

    def GetCurrentSlide(self):
        currentSlide, index = self.__SlidesReverse.Peek()
        return currentSlide, index


class EpisodeInterface1:
    def __init__(self):
        self.__Theme = Theme()
        Fonts = [90, 80, 70, 60, 50, 40, 30, 20]
        self.FontFamily = ["Microsoft YaHei UI Light", "Ebrima"]
        self.interfaceDirectory = os.getcwd()[0: len(os.getcwd()) - len('\\Main')]
        os.chdir(self.interfaceDirectory)
        padding = 80
        self.DirectoryHandler = DirectoryHandler()

        self.InterfaceWindow = Tk()
        self.InterfaceWindow.overrideredirect(1)
        self.InterfaceWindow.attributes("-topmost", True)
        self.InterfaceWindow.config(bg="black")

        sizing = sizingAdjust(self.InterfaceWindow, Fonts, self.FontFamily, padding, self.interfaceDirectory)
        self.sizing = sizing
        self.padding = sizing.padding
        self.screenWidth = sizing.width
        self.screenHeight = sizing.height
        self.FontSize = sizing.FontSize

        self.createEpisode()

        geometry = str(sizing.width1) + "x" + str(sizing.height1) + "+0+0"
        self.InterfaceWindow.geometry(geometry)

        self.ScreenCanvas = Frame(self.InterfaceWindow)
        self.ScreenCanvas.place(relx=sizing.canvasPosX, rely=sizing.canvasPosY, width=self.screenWidth,
                                height=self.screenHeight)

        self.createEpisode()

        threading.Thread(target=self.InterfaceWindow.mainloop(), args=()).start()

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

        episodeText11 = "You are stopped by another man on the other corner"
        episodeText12 = "Going somewhere?"
        episodeText13 = "Let’s see how tough you are by the time I’m finished with…"

        Slide1 = SlideData("narration", ["market.png", episodeText1, "TC"])
        Slide2 = SlideData("narration", ["market.png", episodeText2, "TC"])
        Slide3 = SlideData("convo", ["market.png", "guard1", episodeText3])
        Slide4 = SlideData("convo", ["market.png", "guard2", episodeText4])
        Slide5 = SlideData("narration", ["street1.png", episodeText5, "TC"])
        Slide6 = SlideData("narration", ["street1.png", episodeText6, "TC"])
        Slide7 = SlideData("narration", ["street1.png", episodeText7, "TC"])
        Slide8 = SlideData("convo", ["street1.png", "villain1", episodeText8])
        Slide9 = SlideData("narration", ["street1.png", episodeText9, "TC"])

        slideArray = [Slide2, Slide3, Slide4, Slide5, Slide6, Slide7, Slide8]

        self.Episode = Episode(Slide1, self.InterfaceWindow, self.sizing)

        for slide in slideArray:
            self.Episode.AddSlide(slide, self.InterfaceWindow, self.sizing)

        self.Episode.StartEpisode()

        #self.InterfaceWindow.bind("<space>", lambda event: self.moveToPreviousSlide(event))
        self.InterfaceWindow.bind("<Key>", lambda event: self.moveToNextSlide(event))



if __name__ in '__main__':
    Main = EpisodeInterface1()