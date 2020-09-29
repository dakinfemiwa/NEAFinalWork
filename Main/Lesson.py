import tkinter
from tkinter import *
from sizingAdjust import sizingAdjust
from DirectoryHandler import DirectoryHandler
import os
from Tools.story import SlideData
from Tools.story import Episode
import threading

class ProjectileLessonMain:
    def __init__(self, window, sizing, user):
        #Set attributes
        self.InterfaceWindow = window
        self.Fonts = [90, 80, 70, 60, 50, 40, 30, 20]
        self.FontFamily = ["Microsoft YaHei UI Light", "Ebrima"]
        #Sets directory to the correct direcory for the DirectoryHandler Module
        self.interfaceDirectory = os.getcwd()
        os.chdir(self.interfaceDirectory)
        self.padding = 80
        self.sizing = sizing
        self.user = user

        #Implements the purpose of the lesson
        #Gathers text together
        self.__OrganiseSlides()

    def __OrganiseSlides(self):
        ##################################################
        #   Organising all the texts for the convo slides
        ##################################################

        self.__Slides = []

        #1. Introduction slide
        ProjectileSlideText1 = 'Hi! I’m Coach, and I’ll be teaching you this content.'
        ProjectileSlideText2 = 'We’ll take you through the basic skills you need to reach your dream '
        ProjectileSlideText3 = 'First thing first shooting'
        ProjectileSlideText4 = 'It’s the final NBA match. Every point counts. You have the ball in your hand.'
        ProjectileSlideText5 = 'How would you make sure you would get the ball in?'
        ProjectileSlideText6 = 'First thing is speed. You have to release the ball at the right speed.'
        ProjectileSlideText7 = 'To know that we need to study the properties of the ball'

        self.introBg = [ProjectileSlideText2, ProjectileSlideText3, ProjectileSlideText4, ProjectileSlideText5, ProjectileSlideText6, ProjectileSlideText7]

        Slide1 = SlideData("convo", ["gameIntro.png", "coach", ProjectileSlideText1])

        for text in self.introBg:
            newSlide = SlideData("convo", ["gameIntro.png", "coach", text])
            self.__Slides.append(newSlide)

        #2. First Diagram - Projectile Diagram1 (Basically a ball with a diagram pointing to its weight)
        ProjectileSlideText8 = 'The first thing to recognise is that the ball has weight going downwards.'
        ProjectileSlideText9  = 'If there’s no air resistance this is the only force acting on it.'
        ProjectileSlideText10 = 'This is an example of a projectile- objects that are only acted on by the force of gravity.'

        diagram1 = [ProjectileSlideText8, ProjectileSlideText9, ProjectileSlideText10]

        for text in diagram1:
            newSlide = SlideData("convo", ["speedParabola.png", "coach", text])
            self.__Slides.append(newSlide)

        #3. Second Diagram - Projectile Diagram2 (Shows the velocities from the ball)
        ProjectileSlideText11 = 'Gravity acts downwards and so the ball accelerates downwards.'
        ProjectileSlideText12 = 'However there is no force acting on it horizontally.'

        diagram2 = [ProjectileSlideText11, ProjectileSlideText12]

        for text in diagram2:
            newSlide = SlideData("convo", ["speedResolved.png", "coach", text])
            self.__Slides.append(newSlide)

        #4. Third Diagram - Projectile Diagram3 (Shows velocities and parabola diagram)
        ProjectileSlideText13 = 'As the ball is being projected upwards it has a horizontal velocity'
        ProjectileSlideText14 = 'This velocity remains constant.'
        ProjectileSlideText15 = 'The reason why it goes up and goes down is because as it accelerates downwards it decelerates upwards'
        ProjectileSlideText16 = 'The upwards velocity reaches zero and then increases downwards'
        ProjectileSlideText17 = 'The shape formed is a parabola'

        diagram3 = [ProjectileSlideText13, ProjectileSlideText14, ProjectileSlideText15, ProjectileSlideText16, ProjectileSlideText17]

        for text in diagram3:
            newSlide = SlideData("convo", ["speedParabola.png", "coach", text])
            self.__Slides.append(newSlide)

        #5. Fourth Diagram - Projectile Diagram4 (Shows a vector velocity being resolved
        ProjectileSlideText18 = 'Note that velocity is a vector and can be resolved if it’s direction is at an angle to the horizontal or vertical.'
        ProjectileSlideText19 = 'So here the 15ms¯¹ can be resolved horizontally so the horizontal speed is 15cos(30) = 13ms¯¹ (2sf) and 15sin(30)=7.5ms¯¹'
        ProjectileSlideText20 = 'And that’s how the speed works'

        diagram4 = [ProjectileSlideText18, ProjectileSlideText19, ProjectileSlideText20, 'END']

        for text in diagram4:
            newSlide = SlideData("convo", ["speedResolved.png", "coach", text])
            self.__Slides.append(newSlide)

        #6. Fifth Diagram - Shows graph of velocity against time and shows derivation of formulas
        ProjectileSlideText21 = 'Because the force of gravity is constant it’s speed would be constant as well.'
        ProjectileSlideText22 = 'The displacement is also known as the area under the graph and so the speed of it will be the area of a trapezium- ½ × (u+v) × t.'
        ProjectileSlideText23 = 'The gradient acceleration can be calculated as a = (v-u)/t'
        ProjectileSlideText24 = 'This can be rearranged to v=u + at and subbing that in gives us another formula of s=ut+ ½at2.'
        ProjectileSlideText25 = 'We can know calculate what speed to project it.'

        diagram5 = [ProjectileSlideText21, ProjectileSlideText22, ProjectileSlideText23, ProjectileSlideText24, ProjectileSlideText25]

        for text in diagram5:
            newSlide = SlideData("convo", ["velocityAgainstTime.png", "coach", text])
            self.__Slides.append(newSlide)

        #7. Sixth Diagram - Shows diagram of ball and workings to find speed
        #   Diagram also to contain a Note: For this question we have assumed the angle is 30 degrees from the horizonal
        ProjectileSlideText26 = 'We resolve the velocity we can get the horizontal velocity'

        ProjectileSlideText27 = 'We can then sub it into the formula  time = distance divided by speed to get the time'
        ProjectileSlideText28 = 'Then we can use that time and our other formulas to calculate the speed'
        ProjectileSlideText29 = 'And there\'s the speed!'
        ProjectileSlideText30 = 'Press the right key to return to menu!'

        diagram6 = [ProjectileSlideText27, ProjectileSlideText28, ProjectileSlideText29, ProjectileSlideText30]

        for text in diagram6:
            newSlide = SlideData("convo", ["workings.png", "coach", text])
            self.__Slides.append(newSlide)

        self.Episode = Episode(Slide1, self.InterfaceWindow, self.sizing)

        for slide in self.__Slides:
            self.Episode.AddSlide(slide, self.InterfaceWindow, self.sizing)

        self.Episode.StartEpisode()
        self.InterfaceWindow.bind("<Key>", lambda event: self.moveToNextSlide(event))

    def moveToNextSlide(self, event):
        try:
            if event.keysym == "Right":
                try:
                    self.Episode.NextSlide()
                except TypeError:
                    self.InterfaceWindow.bind("<Key>", lambda event: self.blankMethod())
                    self.ReturnToMenu()

            elif event.keysym == "Left":
                try:
                    self.Episode.PreviousSlide()
                except TypeError:
                    print("returning to projectile menu")
                    from Intro import ProjectileGameIntro
                    ProjectileGameIntro(self.InterfaceWindow, self.sizing, self.user)
        except:
            self.ReturnToGameMenu()

    def ReturnToMenu(self):
        #Returns to court once lesson is over
        from Menu import BasketballCourt
        BasketballCourt(self.InterfaceWindow, self.sizing, self.user)

    def ReturnToGameMenu(self):
        self.InterfaceWindow.bind("<Key>", lambda event: self.blankMethod())
        from Intro import ProjectileGameIntro
        ProjectileGameIntro(self.InterfaceWindow, self.sizing, self.user)

    def blankMethod(self):
        pass

class MomentumLessonMain:
    def __init__(self, window, sizing, user):
        self.InterfaceWindow = window
        self.sizing = sizing
        self.user = user
        self.Fonts = [90, 80, 70, 60, 50, 40, 30, 20]
        self.FontFamily = ["Microsoft YaHei UI Light", "Ebrima"]
        self.interfaceDirectory = os.getcwd()
        os.chdir(self.interfaceDirectory)
        self.padding = 80
        procceedText = "Press any key to continue"

        self.__OrganiseSlides()

    def __OrganiseSlides(self):
        ##################################################
        #   Organising all the texts for the convo slides
        ##################################################
        self.__Slides = []

        #1. Introduction slide
        introText = 'Hi! I’m Coach, and I’ll be teaching you this content.'
        ProjectileSlideText1 = 'Every basketball has mass'
        ProjectileSlideText2 = 'If it\'s moving it also has velocity'
        ProjectileSlideText3 = 'This means it has momentum'
        ProjectileSlideText4 = 'momentum  = mass × velocity'

        self.bg1 = [ProjectileSlideText1, ProjectileSlideText2, ProjectileSlideText3, ProjectileSlideText4]

        Slide1 = SlideData("convo", ["basketballProjectileBackground2.png", "coach", introText])

        for text in self.bg1:
            newSlide = SlideData("convo", ["basketballProjectileBackground2.png", "coach", text])
            self.__Slides.append(newSlide)

        self.Episode = Episode(Slide1, self.InterfaceWindow, self.sizing)

        for slide in self.__Slides:
            self.Episode.AddSlide(slide, self.InterfaceWindow, self.sizing)

        self.Episode.StartEpisode()
        self.InterfaceWindow.bind("<Key>", lambda event: self.moveToNextSlide(event))

    def moveToNextSlide(self, event):
        try:
            if event.keysym == "Right":
                try:
                    self.Episode.NextSlide()
                except TypeError:
                    self.InterfaceWindow.bind("<Key>", lambda event: self.blankMethod())
                    self.ReturnToMenu()

            elif event.keysym == "Left":
                try:
                    self.Episode.PreviousSlide()
                except:
                    self.InterfaceWindow.bind("<Key>", lambda event: self.blankMethod())
                    self.ReturnToGameMenu()
        except:
            self.ReturnToMenu()

    def ReturnToMenu(self):
        #Returns to court once lesson is over
        from Menu import BasketballCourt
        BasketballCourt(self.InterfaceWindow, self.sizing, self.user)

    def ReturnToGameMenu(self):
        from Intro import MomentumLessonIntro
        MomentumLessonIntro(self.InterfaceWindow, self.sizing, self.user)

    def blankMethod(self):
        pass


    def __GoBackToMenu(self, event):
        from Menu import BasketballCourt
        BasketballCourt(self.InterfaceWindow, self.sizing, self.user)


class EllipseLessonMain:
    def __init__(self, window, sizing, user):
        # Gathers neccessart attributes and fixes directories
        self.InterfaceWindow = window
        self.sizing = sizing
        self.user = user
        self.Fonts = [90, 80, 70, 60, 50, 40, 30, 20]
        self.FontFamily = ["Microsoft YaHei UI Light", "Ebrima"]
        self.interfaceDirectory = os.getcwd()
        self.padding = 80
        procceedText = "Press any key to continue"

        # Brings slides together so they can run in sequence
        self.__OrganiseSlides()

    def __OrganiseSlides(self):
        ##################################################
        #   Organising all the texts for the convo slides
        ##################################################
        self.__Slides = []
        introText = 'Hi! I’m Coach, and I’ll be teaching you this content.'
        # Diagram 1- uses basketballGame.png
        slideText1 = "Is there a way of determining if a player is in range of a 3 pointer?"
        slideText2 = "It's 5 seconds t ot he end of th match. The Lakers are still down by 2 points. Kusma has the ball. He takes a shot and it goes!"
        slideText3 = "How could you determine if Kusma's shot was enough to win the game?\n Let's say we had his coordinates relative to the court"
        slideText4 = "We know if he's on this ellipse he gets the 3 points."

        diagram1 = [slideText1, slideText2, slideText3, slideText4]

        Slide1 = SlideData("convo", ["basketballGame.png", "coach", introText])

        for text in diagram1:
            newSlide = SlideData("convo", ["basketballGame.png", "coach", text])
            self.__Slides.append(newSlide)

        # Diagram 2 - uses basketballGraph.png
        slideText5 = "Let's model our court. Well asumme for now our court models an ellipse."

        newSlide = SlideData("convo", ["basketballGraph.png", "coach", slideText5])
        self.__Slides.append(newSlide)

        # Diagram 3 - uses EllipseGraph.png
        slideText6 = "The formula for an ellipse is always ______"
        slideText7 = "If we sub his x and y coordinates and we get 1, then that means Kusma has won the game."

        diagram3 = [slideText6, slideText7]

        for text in diagram3:
            newSlide = SlideData("convo", ["EllipseGraph.png", "coach", text])
            self.__Slides.append(newSlide)
        self.Episode = Episode(Slide1, self.InterfaceWindow, self.sizing)

        for slide in self.__Slides:
            self.Episode.AddSlide(slide, self.InterfaceWindow, self.sizing)

        self.Episode.StartEpisode()
        self.InterfaceWindow.bind("<Key>", lambda event: self.moveToNextSlide(event))

    def moveToNextSlide(self, event):
        try:
            if event.keysym == "Right":
                try:
                    self.Episode.NextSlide()
                except TypeError:
                    self.InterfaceWindow.bind("<Key>", lambda event: self.blankMethod())
                    self.ReturnToMenu()

            elif event.keysym == "Left":
                try:
                    self.Episode.PreviousSlide()
                except:
                    self.InterfaceWindow.bind("<Key>", lambda event: self.blankMethod())
                    self.ReturnToGameMenu()
        except:
            self.ReturnToMenu()

    def ReturnToMenu(self):
        # Returns to court once lesson is over
        from Menu import BasketballCourt
        BasketballCourt(self.InterfaceWindow, self.sizing, self.user)

    def ReturnToGameMenu(self):
        from Intro import EllipseLessonIntro
        EllipseLessonIntro(self.InterfaceWindow, self.sizing, self.user)

    def blankMethod(self):
        pass
