import os, sys
sys.path.append(os.getcwd() + "\\Tools")
orignialDir = os.getcwd()
try:
    os.chdir(os.getcwd() + "\\Tools")
except:
    pass
from Stack import Stack
os.chdir(orignialDir)
import tkinter
from tkinter import *
import PIL
from PIL import Image
from DirectoryHandler import DirectoryHandler
import shutil
from Stack import Stack

#Module to deal with the sizing of a computer in order to properly execute its full screen
class sizingAdjust:
    def __init__(self, file, fontFamily, fontSize, padding, directory):
        #Creates attributes needed to gather neccessary scrren data
        self.file = file
        #Gets the screen width of device
        self.width1 = file.winfo_screenwidth()
        #Gets the screen height of the device
        self.height1 = file.winfo_screenheight()

        #Sets attribute for the fonts
        self.FontFamily = fontFamily
        self.FontSize = fontSize

        print((self.FontSize, "FONTS"))

        #Sets attributes for the padding
        self.padding = padding

        #Sets attribute for the directory
        self.directory = directory

        #Gets the screen resolution of canvas
        self.getSizeWindow()
        #Determines position screencanvas must be at
        self.determinePos()
        #Resizes the scale of fonts so that fonts do not affect the appearance of the program
        self.makeFonts()
        #Resizes images so that they games can be played
        #self.resizeImages()

    #Module to get the screen size of the screen canvas
    #   The interface of the game works at a 16:9 ratio as do most screens
    def getSizeWindow(self):
        '''This module finds the best fit for a landscape 16:9 screen ratio view'''
        ratio = self.width1 / self.height1
        ##print(ratio)

        if ratio < (16 // 9):
            self.width = self.width1
            self.height = self.width // (16/9)
        else:
            self.height = self.height1
            self.width = self.height1 * (16 / 9)

        self.height = int(round(self.height))
        self.width = int(round(self.width))

    #Determines the position of the screen canvas so that the program can be in line at the centre of the user
    def determinePos(self):
        self.canvasPosY = (self.height1 - self.height) / (2 * self.height1)

        if self.width1 > 4000:
            self.canvasPosX = (self.width1 - 4000) / (2 * self.width)
            self.oversize = True
        else:
            self.canvasPosX = 0
            self.oversize = False

    #Resizes fonts so they readjust to adapt to any normal range screen depending on thier size
    #   Note: This is for a screen with a width between 600 to 1250px. Larger screens should easily adapt to size
    def makeFonts(self):
        if self.width1 >=600 and self.width1 <=675:
            for font in self.FontSize:
                self.FontSize[i] = float(self.FontSize[i])
                i = self.FontSize.index(font)
                self.FontSize[i] *= (self.width1 / 1650)
                self.FontSize[i] = int(round(self.FontSize[i]))
                self.padding  *= (self.width1 / 1650)
        elif self.width1 < 750:
            for font in self.FontSize:
                i = self.FontSize.index(font)
                self.FontSize[i] = float(self.FontSize[i])
                self.FontSize[i] *= (self.width1 / 1600)
                self.FontSize[i] = int(round(self.FontSize[i]))
                self.padding  *= (self.width1 / 1600)
        elif self.width1 < 1000:
            for font in self.FontSize:
                i = self.FontSize.index(font)
                self.FontSize[i] = float(self.FontSize[i])
                self.FontSize[i] *= (self.width1 / 1650)
                self.FontSize[i] = int(round(self.FontSize[i]))
                self.padding  *= (self.width1 / 1650)
        elif self.width1 <= 1200:
            for font in self.FontSize:
                i = self.FontSize.index(font)
                self.FontSize[i] = float(self.FontSize[i])
                self.FontSize[i] *= (self.width1 / 1550)
                self.FontSize[i] = int(round(self.FontSize[i]))
                self.padding *= (self.width1 / 1550)
        elif self.width1 < 1250:
            for font in self.FontSize:
                i = self.FontSize.index(font)
                self.FontSize[i] = float(self.FontSize[i])
                self.FontSize[i] *= (self.width1 / 1250)
                self.FontSize[i] = int(round(self.FontSize[i]))
                self.padding *= (self.width1 / 1250)

    #Resizes background images so they can fit to any type of screen, works per list of images
    def resizeSetImages(self, images, h, w):
        #For every image
        for image in images:
            #Renames current image
            os.rename(image, "OLD" + image)
            billboardImage = Image.open("OLD" + image)

            #Gathers data on the new height and width of the images
            newHeight = int (round(h))
            newWidth =  int (round(w))

            if image == "background1Img.png":
                newHeight = int(round(h * 1.1))
                newWidth =  int(round(w * 1.1))

            newSize = (newWidth, newHeight)

            #Resizes the image and then saves it as it's original name
            try:
                billboardImage = billboardImage.resize(newSize, Image.ANTIALIAS)
                billboardImage.save(image)

            #If the image cannot be found then it recreates the old file
            except OSError:
                shutil.copyfile("OLD"+image, image)

            #Old file is then removed
            os.remove("OLD" + image)

    #Modules that handle the sizes for each image folder
    def resizeImages(self):
        #Checks if the images have been resized by 'certificate' indicating that
        try:
            file = open("resized.txt", "r+")
            #print("Images already resized")
            return False
        except FileNotFoundError:
            pass

        # Resizes for BackgroundImages
        #Changes directory so that images can be accessed
        self.DirectoryHandler = DirectoryHandler()
        self.DirectoryHandler.changeDirectoryToBackground()
        self.DirectoryHandler.changeDirectoryToMain()
        #Returns list of images in directory
        images = self.DirectoryHandler.findImages()
        #Resizes set of images
        self.resizeSetImages(images, self.height1, self.width1)
        #Resets directory to original directory
        self.DirectoryHandler.changeDirectoryToMain()

        #Avatars
        # BackgroundImages
        #Changes directory so that images can be accessed
        self.DirectoryHandler = DirectoryHandler()
        self.DirectoryHandler.changeDirectoryToAvatar()
        # Returns list of images in directory
        images = self.DirectoryHandler.findImages()
        # Resets directory to original directory
        self.resizeSetImages(images, self.height1 * .45, self.height1 * .45)
        self.DirectoryHandler.changeDirectoryToMain()

        #Diagrams
        # Changes directory so that images can be accessed
        self.DirectoryHandler = DirectoryHandler()
        self.DirectoryHandler.changeDirectoryToLessons()
        # Returns list of images in directory
        images = self.DirectoryHandler.findImages()
        # Resets directory to original directory
        self.resizeSetImages(images, self.height1 * .75, self.height1 * .75)
        self.DirectoryHandler.changeDirectoryToMain()

        #GameBackgrounds
        # Changes directory so that images can be accessed
        self.DirectoryHandler = DirectoryHandler()
        self.DirectoryHandler.changeDirectoryToBackgroundGame()
        # Returns list of images in directory
        images = self.DirectoryHandler.findImages()
        # Resets directory to original directory
        self.resizeSetImages(images, self.height1, self.width1 * 3)
        self.DirectoryHandler.changeDirectoryToMain()

        #GameBackgroundsNA
        # Changes directory so that images can be accessed
        self.DirectoryHandler = DirectoryHandler()
        self.DirectoryHandler.changeDirectoryToBackgroundGameNA()
        # Returns list of images in directory
        images = self.DirectoryHandler.findImages()
        # Resets directory to original directory
        self.resizeSetImages(images, self.height1, self.width1)
        self.DirectoryHandler.changeDirectoryToMain()

        #Issues 'certificate' to avoid resizing already truncated files
        file = open("resized.txt", "w")