import tkinter
from tkinter import *
from Tools.sizingAdjust import sizingAdjust
from Slide import Slide
from Theme import Theme
from Slide import Welcome
from Slide import LoginPage
from Slide import Lesson
from Slide import GameRunaway
from Stack import Stack
from Slide import Convo
from Tools.DirectoryHandler import DirectoryHandler
import os
import threading

class Main:
    def __init__(self, window):
        self.__Theme = Theme()
        self.InterfaceWindow = window
        self.FontSizes = [90, 80, 70, 60, 50, 40, 30, 20]
        self.FontFamily = ["Microsoft YaHei UI Light", "Ebrima", "Courier New"]
        self.interfaceDirectory = os.getcwd()[0: len(os.getcwd()) - len('\\Main')]
        os.chdir(self.interfaceDirectory)
        self.padding = 80
        procceedText = "Press any key to continue"

        self.__CreateWindow()
        self.__OrganiseSlides()


    def __CreateWindow(self):

        self.InterfaceWindow.overrideredirect(1)
        self.InterfaceWindow.attributes("-topmost", True)
        self.InterfaceWindow.config(bg="black")

        self.sizing = sizingAdjust(self.InterfaceWindow, self.FontFamily, self.FontSizes, self.padding, self.interfaceDirectory)
        geometry = str(self.sizing.width) + "x" + str(self.sizing.height) + "+0+0"
        self.InterfaceWindow.geometry(geometry)

    def __OrganiseSlides(self):
        if __name__ in '__main__':
            welcomeSlide = Welcome(self.InterfaceWindow, self.sizing, "backgroundImg1.png")
            threading.Thread(target=welcomeSlide.viewSlide(), args=()).start()

            self.InterfaceWindow.bind("<Key>", lambda event: self.__LoginPage(event))

    def __LoginPage(self, event):
        print(os.getcwd())
        loginSlide = LoginPage(self.InterfaceWindow, self.sizing, "backgroundImg1.png")
        threading.Thread(target=loginSlide.viewSlide(), args=()).start()



if __name__ in '__main__':
    file = Tk()
    Main(file)

threading.Thread(target=file.mainloop(), args=()).start()
