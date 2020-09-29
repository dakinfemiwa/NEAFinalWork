from tkinter import ttk
from tkinter import *
from sizingAdjust import sizingAdjust
from Tools.DirectoryHandler import DirectoryHandler
from Tools.DataHandler import DataHandler
from Tools.User import User
from Tools.Tree import Tree
from Tools.Theme import Theme
import os
import threading
from Game import BoardGame


class Settings:
    def __init__(self, window, sizing, user):
        self.__Tasks = []
        self.__user = user
        
        self.__Theme = Theme()


        Fonts = [90, 80, 70, 60, 50, 40, 30, 20]
        self.__FontFamily = ["Microsoft YaHei UI Light", "Ebrima"]
        self.__interfaceDirectory = os.getcwd()

        self.__InterfaceWindow = window

        sizing = sizing
        self.__padding = sizing.padding
        self.__screenWidth = sizing.width
        self.__screenHeight = sizing.height

        self.__canvasWidth = .9 * self.__screenWidth
        self.__canvasHeight = .9 * self.__screenHeight

        self.__FontSize = sizing.FontSize
        self.__sizing = sizing

        geometry = str(sizing.width) + "x" + str(sizing.height) + "+0+0"
        self.__InterfaceWindow.geometry(geometry)

        self.__DirectoryHandler = DirectoryHandler()
        self.__DataHandler = DataHandler()

        self.__DirectoryHandler.changeDirectoryToBackground()
        print(os.getcwd())
        Background = PhotoImage(file="backgroundImg1.png")
        self.__DirectoryHandler.changeDirectoryToMain()

        self.__ScreenCanvas = Canvas(self.__InterfaceWindow)
        self.__ScreenCanvas.place(relx=sizing.canvasPosX, rely=sizing.canvasPosY, width=self.__screenWidth,
                                height=self.__screenHeight)

        BackgroundLabel = Label(self.__ScreenCanvas, image=Background)
        BackgroundLabel.place(relx=0, rely=0, width=self.__screenWidth, height=self.__screenHeight)

        fontStyle = (self.__FontFamily[1], self.__FontSize[5])

        self.__InfoCanvas = Frame(self.__ScreenCanvas, bg=self.__Theme.getBackground1())#, font=fontStyle)
        self.__InfoCanvas.place(relx=.05, rely=.05, width=.9 * self.__screenWidth, height=.9 * self.__screenHeight)

        self.__ButtonFrame = Frame(self.__InfoCanvas, bg=self.__Theme.getBackground3())
        self.__ButtonFrame.place(relx=0, rely=0, width=.3*self.__canvasWidth, height=self.__canvasHeight)

        self.__AvatarButton = Frame(self.__InfoCanvas, bg=self.__Theme.getBackground3b(), cursor="hand2")
        self.__AvatarButton.place(relx=0, rely=0, width=.3*self.__canvasWidth, height=.15*self.__canvasHeight)


        AvatarTextStr = "Customise Avatar"
        AvatarDescriptionStr = "Choose and customise your avatar"

        self.__AvatarText, self.__AvatarDescription = self.__createButton(AvatarTextStr, AvatarDescriptionStr,
                                                                    self.__AvatarButton)

        self.__ChangeLoginButton = Frame(self.__InfoCanvas, bg=self.__Theme.getBackground3b(), cursor="hand2")
        self.__ChangeLoginButton.place(relx=0, rely=.155, width=.3*self.__canvasWidth, height=.15*self.__canvasHeight)

        ChangePasswordStr = "Edit Login Details"
        ChangePasswordDescription = "Change your username/password"

        self.__ChangeLoginText, self.__ChangeLoginLbl = self.__createButton(ChangePasswordStr, ChangePasswordDescription,
                                                                               self.__ChangeLoginButton)

        self.__FriendsButton = Frame(self.__InfoCanvas, bg=self.__Theme.getBackground3b(), cursor="hand2")
        self.__FriendsButton.place(relx=0, rely=.31, width=.3*self.__canvasWidth, height=.15*self.__canvasHeight)

        FriendsStr = "Friends"
        FriendsDescriptionStr = "Find and add friends"

        self.__FriendsTextTitle, self.__FriendsLbl = self.__createButton(FriendsStr, FriendsDescriptionStr, self.__FriendsButton)

        ReturnToMenuStr = "Return to Menu"
        ReturnToMenuDescriptionStr = "Exit Settings"

        self.__ReturnToMenuButton = Frame(self.__InfoCanvas, bg=self.__Theme.getBackground3b(), cursor="hand2")
        self.__ReturnToMenuButton.place(relx=0, rely=.620, width=.3*self.__canvasWidth, height=.15*self.__canvasHeight)

        self.__ReturnToMenuTitle, self.__FriendsLbl = self.__createButton(ReturnToMenuStr, ReturnToMenuDescriptionStr, self.__ReturnToMenuButton)

        """DarkModeStr = "Change Mode"
        DarkModeDescriptionStr = "Customise the interface as you feel"

        self.__DarkModeButton = Frame(self.__InfoCanvas, bg=self.__Theme.getBackground3b(), cursor="hand2")
        self.__DarkModeButton.place(relx=0, rely=.465, width=.3 * self.__canvasWidth,
                                        height=.15 * self.__canvasHeight)

        self.__DarkModeButtonTitle, self.__DarkModeButtonLbl = self.__createButton(DarkModeStr, DarkModeDescriptionStr, self.__DarkModeButton)
            """
        self.__createSettingFrame()

        self.__InterfaceWindow.bind("<Key>", lambda event: self.__navigateKey(event))
        self.__InterfaceWindow.bind("<Button-1>", lambda event: self.__navigateClick(event))

        threading.Thread(target=self.__InterfaceWindow.mainloop(), args=()).start()

    def __createSettingFrame(self):
        title = "Settings"
        self.__MainSettingsFrame, self.__MainSettingsTitle = self.__createFrame(title)

        username = self.__user.getUsername()
        coins = self.__user.getCoins()
        avatar = self.__user.getAvatar()
        avatarURL = self.__DataHandler.getAvatarURL(avatar)

        self.__DirectoryHandler.changeDirectoryToAvatar2()
        AvatarImage = PhotoImage(file=avatarURL)
        self.__DirectoryHandler.changeDirectoryToMain()

        LoginDetails = f'Username: {username}\nCoins: {coins}'

        LoginDetailsFrame = Frame(self.__MainSettingsFrame, bg=self.__Theme.getBackground2())
        LoginDetailsFrame.place(relx=.05, rely=.25, width = .9 *self.__canvasWidth,
                                height=(200/768)*self.__screenHeight)

        LoginDetailsAvatar = Label(LoginDetailsFrame, image=AvatarImage)
        LoginDetailsFrame.image = AvatarImage
        LoginDetailsAvatar.place(relx=.0, rely=0)

        loginDetailsFont = (self.__FontFamily[0], self.__FontSize[6])
        LoginDetailsMessage = Message(LoginDetailsFrame, text=LoginDetails, font=loginDetailsFont, bg=self.__Theme.getBackground2(),
                                      fg=self.__Theme.getForeground1(), width=int(round(550*(self.__screenWidth / 1366)))  )
        LoginDetailsMessage.place(relx=.25, rely=.05)

        Notifications = self.__user.getNotifications()

        NotificationsFrame = Frame(self.__MainSettingsFrame, bg=self.__Theme.getBackground2(),
                                     width=int(round(650*(self.__screenWidth / 1366))))
        NotificationsFrame.place(relx=.05, rely=.55, width = .9 *self.__canvasWidth,
                                height=(200/768)*self.__screenHeight)

        NotificationsText = Label(NotificationsFrame, font=loginDetailsFont, bg=self.__Theme.getBackground2(), fg=self.__Theme.getForeground1())
        NotificationsText.place(relx=.05, rely=.05)

        NotificationsStr = ''

        print(Notifications)

        if Notifications == None:
            NotificationsStr = 'You have no new notifications'
            NotificationsText.place(relx=.05, rely=.45)
        else:
            for notification in Notifications:
                NotificationsStr = NotificationsStr + "- " + str(notification[0]) + "\n"

            self.__user.clearNotifications()


        NotificationsText['text'] = NotificationsStr

    def __createButton(self, title, description, button):
        fontStyleLabel = (self.__FontFamily[0], self.__FontSize[6], "bold", "underline")
        fontStyleDescription = (self.__FontFamily[0], int(round(self.__FontSize[6] * 0.5)) )

        TextLabel= Label(button, text=title, font=fontStyleLabel, bg=self.__Theme.getBackground3b(), fg=self.__Theme.getForeground1())
        TextLabel.place(relx=.05, rely=.005)

        TextDescription = Message(button, text=description, font=fontStyleDescription, bg=self.__Theme.getBackground3b(),
                                  width= 320 * (self.__screenWidth / 1366))
        TextDescription.place(relx=.025, rely=.55)

        return TextLabel, TextDescription


    def __navigateKey(self, event):
        if event.keysym.upper() == "X":
            from Menu import Main
            Main(self.__InterfaceWindow, self.__sizing, self.__user)
            return

    def __navigateClick(self, event):
        if event.widget == self.__AvatarButton or event.widget == self.__AvatarText or event.widget == self.__AvatarDescription or event.widget == self.__ChangeLoginButton or event.widget == self.__ChangeLoginLbl or event.widget == self.__ChangeLoginText or event.widget == self.__FriendsButton or event.widget == self.__FriendsTextTitle or event.widget == self.__FriendsLbl:
            try:
                self.__AvatarFrame.destroy()
            except:
                pass

            try:
                self.__ChangeLoginFrame.destroy()
            except:
                pass

            try:
                self.__FriendsFrame.destroy()
            except:
                pass

        if event.widget  == self.__AvatarButton or event.widget == self.__AvatarText or event.widget == self.__AvatarDescription:
            #View Avatar Button
            title = "Avatars"
            userID = self.__user.getUserID()
            userAvatar = self.__user.getAvatar()
            self.__AvatarFrame, self.__AvatarFrameTitle = self.__createFrame(title)

            self.__avatars = self.__DataHandler.getAvatarInfo()

            for avatar in self.__avatars:
                index = self.__avatars.index(avatar)
                if avatar[0] == userAvatar:
                    break

            avatarURL = self.__DataHandler.getAvatarURL(userAvatar)

            self.__DirectoryHandler.changeDirectoryToAvatar()
            avatarPhotoImage = PhotoImage(file=avatarURL)
            self.__DirectoryHandler.changeDirectoryToMain()

            self.__AvatarPlaceHolder = Label(self.__AvatarFrame, bg=self.__Theme.getBackground3(), image=avatarPhotoImage)
            self.__AvatarPlaceHolder.place(relx=(1/2 - ((346/1.9) /(.9* 1366))), rely=(1/3), width= 346 * (self.__canvasWidth/1366))
            self.__AvatarPlaceHolder.image = avatarPhotoImage

            buttonFont = (self.__FontFamily[0], int(round(self.__FontSize[7] * 1.5)))

            self.__LeftButton = Button(self.__AvatarFrame, text="<", bd=0, font=buttonFont, bg=self.__Theme.getBackground1(),
                                     command=lambda: self.__changeAvatarIndex("-"))
            self.__LeftButton.place(relx=(1/2 - (350/1366)), rely=(1/2))

            self.__RightButton = Button(self.__AvatarFrame, text=">", bd=0, font=buttonFont, bg=self.__Theme.getBackground1(),
                                     command=lambda: self.__changeAvatarIndex("+"))
            self.__RightButton.place(relx=(1/2 + (350/1366)), rely=(1 / 2))

            self.__avatarIndex = index

            fontSize = (self.__FontFamily[0], int(round(self.__FontSize[7] * 0.5)))

            self.__AvatarPricePlaceHolder = Button(self.__AvatarFrame, bg="black", fg="white", text="hfs", font=fontSize,
                                                 command=lambda: self.__buy(), bd=0, cursor="hand2")
            self.__AvatarPricePlaceHolder.place(relx=(1/2 - ((346/1.9) /(.9* 1366))), rely=((1/3) + (356/ (766))), width= 346 * (self.__canvasWidth/1366))

            self.__AvatarPricePlaceHolder['text'] = str(self.__avatars[self.__avatarIndex][2]) + " coins"


        elif event.widget == self.__ChangeLoginButton or event.widget == self.__ChangeLoginLbl or event.widget == self.__ChangeLoginLbl:
            #View Change Password
            title = "Change Login"
            self.__ChangeLoginFrame, self.__ChangeLoginTitle = self.__createFrame(title)

            UsernameStr = "Change Username:"
            PasswordStr = "Change Password:"
            PasswordRStr = "Confirm New Password:"

            self.__UsernameLabel, self.__UsernameEntry, self.__UsernameSubmit = self.__CreateFormEntry(self.__ChangeLoginFrame,
                                                                                               UsernameStr, 0.3, False)
            self.__PasswordLabel, self.__PasswordEntry, self.__PasswordSubmit = self.__CreateFormEntry(self.__ChangeLoginFrame,
                                                                                               PasswordStr, 0.525, True)
            self.__PasswordRLabel, self.__PasswordREntry, self.__PasswordRSubmit = self.__CreateFormEntry(self.__ChangeLoginFrame,
                                                                                                  PasswordRStr, 0.725,
                                                                                                  True)

            self.__PasswordRSubmit.destroy()

            self.__UsernameSubmit.config(command=lambda: self.__checkChangeUsername(self.__UsernameEntry.get()) )
            self.__PasswordSubmit.config(command=lambda: self.__checkChangePassword(self.__PasswordEntry.get(),
                                                                                self.__PasswordREntry.get()))

        elif event.widget == self.__FriendsButton or event.widget == self.__FriendsLbl or event.widget == self.__FriendsLbl:
            #View Friends Button
            title = "Friends "
            self.__FriendsFrame, self.__FriendsTitle = self.__createFrame(title)

            #Gather fonts together
            buttonFont = (self.__FontFamily[0], self.__FontSize[7], "underline")

            #1. View Friends
            text = "View Friends"
            self.__ViewFriendsButton = Button(self.__FriendsFrame, text=text, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(), font=buttonFont,
                                            command=lambda: self.__viewFriends(), bd=1, relief="solid",
                                            padx=5, pady=5, cursor="hand2")
            self.__ViewFriendsButton.place(relx=.05, rely=.25, width=.18*self.__canvasWidth)

            #2. Find Friends
            text = "Find Friends"
            self.__FindFriendsButton = Button(self.__FriendsFrame, text=text, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(), font=buttonFont,
                                            command=lambda: self.__findFriends(), bd=1, relief="solid",
                                            padx=5, pady=5, cursor="hand2")
            self.__FindFriendsButton.place(relx=.05+(6/7*.3), rely=.25, width=.18*self.__canvasWidth)

            #3. Requests
            text = "View Requests"
            self.__RequestsButton = Button(self.__FriendsFrame, text=text, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(), font=buttonFont,
                                            command=lambda: self.__viewRequests(), bd=1, relief="solid",
                                            padx=5, pady=5, cursor="hand2")
            self.__RequestsButton.place(relx=.05+(12/7*.3), rely=.25, width=.21*self.__canvasWidth)


            """elif event.widget == self.__DarkModeButton or event.widget == self.__DarkModeButtonLbl or event.widget == self.__DarkModeButtonTitle:
            #View Dark Theme avatar
            title = "Appearance "
            self.__AppearanceFrame, self.__AppearanceTitle = self.__createFrame(title)
            theme = "light"
            
            #self.__ModeLabel, self.__ModeCheckbox = self.__createOption("Choose theme", theme, ["Dark", "light"], .3)
            
            #self.__ModeCheckbox.bind("<Button-1>", lambda: self.changeMode())"""

        elif event.widget == self.__ReturnToMenuButton or event.widget == self.__ReturnToMenuTitle or event.widget== self.__FriendsLbl:
            self.__DirectoryHandler.changeDirectoryToMainFolder()
            from Menu import Main
            self.__DirectoryHandler.changeDirectoryToMain()
            Main(self.__InterfaceWindow, self.__sizing, self.__user)

        elif event.widget == self.__ButtonFrame:
            try:
                self.__createSettingFrame()
            except:
                pass

    def changeMode(self):
        newMode = self.__ModeCheckbox.get()
        self.__Theme.changeTheme(newMode)

    def __createOption(self, text, chosenOption, options, yPos):
        fontTitle = (self.__FontFamily[0], self.__FontSize[7])
        optionTitleLbl = Label(self.__AppearanceFrame, text=text, font=fontTitle, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1())
        optionTitleLbl.place(relx=.05, rely=yPos)

        firstOption = StringVar()
        firstOption.set(chosenOption)

        optionsCheckbox = ttk.Combobox(self.__AppearanceFrame, textvariable=firstOption, background="white", foreground="black",
                                   font=fontTitle, state="readonly", cursor="hand2")
        optionsCheckbox.place(relx=.5, rely=yPos)

        optionsCheckbox['values'] = options

        return optionTitleLbl, optionsCheckbox

    def __ColourButton(self, selectedButton):
        buttons = [self.__ViewFriendsButton, self.__FindFriendsButton,  self.__RequestsButton]
        for button in buttons:
            if selectedButton == button:
                button.config(bg=self.__Theme.getBackground2())
            else:
                button.config(bg=self.__Theme.getBackground1())

    def __viewRequests(self):
        self.__ColourButton(self.__RequestsButton)
        self.__viewRequestsFrame, self.__viewRequestsTitle = self.__createFriendsFrame("View Requests")

        print(self.__user.getUserID())
        userID = self.__user.getUserID()
        
        self.__numberOfRequests = self.__user.getNumberOfRequests()
        self.__UserRequests = self.__user.getRequests()
        print(self.__UserRequests)

        fontStyle = (self.__FontFamily[0], self.__FontSize[7])
        self.__numberOfRequestsPlaceHolder = Label(self.__viewRequestsFrame, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(), font=fontStyle)
        self.__numberOfRequestsPlaceHolder.place(relx=.05, rely=.45)

        if self.__numberOfRequests > 0:
            self.__RequestPlaceHolder = Frame(self.__viewRequestsFrame, bg=self.__Theme.getBackground3())
            self.__RequestPlaceHolder.place(relx=.15, rely=.45, width=.7*.63*self.__canvasWidth,
                                          height=.63*.4*self.__canvasHeight)

            self.__AvatarPlaceHolderRequest = Label(self.__RequestPlaceHolder)
            self.__AvatarPlaceHolderRequest.place(relx=0, rely=0)

            fontStyle = (self.__FontFamily[0], self.__FontSize[7])
            self.__AccountInfoPlaceHolder = Label(self.__RequestPlaceHolder, bg=self.__Theme.getBackground3(), fg=self.__Theme.getForeground1(), font=fontStyle)
            self.__AccountInfoPlaceHolder.place(relx=(200/(.63*1366))+ .15, rely=0)

            buttonFont = (self.__FontFamily[0], int(round(self.__FontSize[7] * 1.5)))

            self.__LeftButton = Button(self.__viewRequestsFrame, text="<", bd=0, font=buttonFont, bg=self.__Theme.getBackground1(),
                                     command=lambda: self.__changeUserIndex("-"), cursor="hand2")
            self.__LeftButton.place(relx=.05, rely=.6)

            self.__RightButton = Button(self.__viewRequestsFrame, text=">", bd=0, font=buttonFont, bg=self.__Theme.getBackground1(),
                                      command=lambda: self.__changeUserIndex("+"), cursor="hand2")
            self.__RightButton.place(relx=.9, rely=.6)

            fontStyle = (self.__FontFamily[1], self.__FontSize[7], "underline")
            self.__AcceptButton = Button(self.__RequestPlaceHolder, text="Accept", font=fontStyle, bd=1, padx=5, pady=5,
                                       relief="solid", bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(), command=lambda: self.__acceptRequest())
            self.__AcceptButton.place(relx=.4,rely=.5)

            self.__DeclineButton = Button(self.__RequestPlaceHolder, text="Decline", font=fontStyle, bd=1, padx=5, pady=5,
                                       relief="solid", bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(), command=lambda: self.__declineRequest())
            self.__DeclineButton.place(relx=.65,rely=.5)


        if self.__numberOfRequests == 0:
            self.__numberOfRequestsPlaceHolder['text'] = 'You have no requests today'
        else:
            self.__numberOfRequestsPlaceHolder.place(relx=.05, rely=.25)
            if self.__numberOfRequests == 1:
                self.__numberOfRequestsPlaceHolder['text'] = 'You have 1 request'
            else:
                self.__numberOfRequestsPlaceHolder['text'] = f'You have {self.__numberOfRequests} requests'

            self.__RequestIndex = 0
            print(self.__UserRequests)
            self.__UserRequesterID = self.__UserRequests[self.__RequestIndex][0]
            UserRequestInfo = self.__DataHandler.getDetaForLogin(self.__UserRequesterID)
            self.__UserRequester = User(UserRequestInfo)
            UserRequestAvatar = self.__UserRequester.getAvatar()

            print((self.__UserRequesterID, UserRequestAvatar, UserRequestInfo))

            UserRequestUsername = self.__UserRequester.getUsername()

            AvatarURL = self.__DataHandler.getAvatarURL(UserRequestAvatar)
            self.__DirectoryHandler.changeDirectoryToAvatar2()
            AvatarPhotoImage = PhotoImage(file=AvatarURL)
            self.__DirectoryHandler.changeDirectoryToMain()
            self.__AvatarPlaceHolderRequest['image'] = AvatarPhotoImage
            self.__AvatarPlaceHolderRequest.image = AvatarPhotoImage

            self.__AccountInfoPlaceHolder['text'] = UserRequestUsername

    def __reloadViewFriends(self):
        self.__viewRequestsFrame.destroy()

        self.__viewRequestsFrame, self.__viewRequestsTitle = self.__createFriendsFrame("View Requests")

        userID = self.__user.getUserID()
        self.__numberOfRequests = self.__user.getNumberOfRequests()
        self.__UserRequests = self.__user.getRequests()
        print(self.__UserRequests)

        fontStyle = (self.__FontFamily[1], self.__FontSize[7])
        self.__numberOfRequestsPlaceHolder = Label(self.__viewRequestsFrame, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(), font=fontStyle)
        self.__numberOfRequestsPlaceHolder.place(relx=.05, rely=.45)


        if self.__numberOfRequests == 0:
            self.__numberOfRequestsPlaceHolder['text'] = 'You have no requests today'
        else:
            self.__numberOfRequestsPlaceHolder.place(relx=.05, rely=.25)

            if self.__numberOfRequests == 1:
                self.__numberOfRequestsPlaceHolder['text'] = 'You have 1 request'
            else:
                self.__numberOfRequestsPlaceHolder['text'] = f'You have {self.__numberOfRequests} requests'

            self.__RequestPlaceHolder = Frame(self.__viewRequestsFrame, bg=self.__Theme.getBackground3())
            self.__RequestPlaceHolder.place(relx=.15, rely=.45, width=.7 * .63 * self.__canvasWidth,
                                          height=.63 * .4 * self.__canvasHeight)

            self.__AvatarPlaceHolderRequest = Label(self.__RequestPlaceHolder)
            self.__AvatarPlaceHolderRequest.place(relx=0, rely=0)

            fontStyle = (self.__FontFamily[1], self.__FontSize[7])
            self.__AccountInfoPlaceHolder = Label(self.__RequestPlaceHolder, bg=self.__Theme.getBackground3(), fg=self.__Theme.getForeground1(), font=fontStyle)
            self.__AccountInfoPlaceHolder.place(relx=(200 / (.63 * 1366)) + .15, rely=0)

            buttonFont = (self.__FontFamily[0], int(round(self.__FontSize[7] * 1.5)))

            self.__LeftButton = Button(self.__viewRequestsFrame, text="<", bd=0, font=buttonFont, bg=self.__Theme.getBackground1(),
                                     command=lambda: self.__changeUserIndex("-"))
            self.__LeftButton.place(relx=.05, rely=.6)

            self.__RightButton = Button(self.__viewRequestsFrame, text=">", bd=0, font=buttonFont, bg=self.__Theme.getBackground1(),
                                      command=lambda: self.__changeUserIndex("+"))
            self.__RightButton.place(relx=.9, rely=.6)

            fontStyle = (self.__FontFamily[1], self.__FontSize[7], "underline")
            self.__AcceptButton = Button(self.__RequestPlaceHolder, text="Accept", font=fontStyle, bd=1, padx=5, pady=5,
                                       relief="solid", bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1())
            self.__AcceptButton.place(relx=.4, rely=.5)

            self.__DeclineButton = Button(self.__RequestPlaceHolder, text="Decline", font=fontStyle, bd=1, padx=5, pady=5,
                                        relief="solid", bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1())
            self.__DeclineButton.place(relx=.65, rely=.5)

            self.__RequestIndex = 0
            print(self.__UserRequests)
            self.__UserRequesterID = self.__UserRequests[self.__RequestIndex][0]
            UserRequestInfo = self.__DataHandler.getDetaForLogin(self.__UserRequesterID)
            self.__UserRequester = User(UserRequestInfo)
            UserRequestAvatar = self.__UserRequester.getAvatar()

            print((self.__UserRequesterID, UserRequestAvatar, UserRequestInfo))

            UserRequestUsername = self.__UserRequester.getUsername()

            AvatarURL = self.__DataHandler.getAvatarURL(UserRequestAvatar)
            self.__DirectoryHandler.changeDirectoryToAvatar2()
            AvatarPhotoImage = PhotoImage(file=AvatarURL)
            self.__DirectoryHandler.changeDirectoryToMain()
            self.__AvatarPlaceHolderRequest['image'] = AvatarPhotoImage
            self.__AvatarPlaceHolderRequest.image = AvatarPhotoImage

            self.__AccountInfoPlaceHolder['text'] = UserRequestUsername


    def __acceptRequest(self):
        UserRequestInfo = self.__DataHandler.getDetaForLogin(self.__UserRequesterID)
        UserRequester = User(UserRequestInfo)
        UserRequestUsername = UserRequester.getUsername()
        acceptMessage = f"Your request to be friends with {UserRequestUsername} has been accepted."
        self.__DataHandler.addNotification(self.__UserRequesterID, acceptMessage)

        self.__user.acceptRequest(self.__UserRequesterID)
        self.__Prompt(f"You are now friends with {UserRequestUsername}!")

        self.__reloadViewFriends()

    def __declineRequest(self):
        UserRequestInfo = self.__DataHandler.getDetaForLogin(self.__UserRequesterID)
        UserRequester = User(UserRequestInfo)
        UserRequestUsername = UserRequester.getUsername()

        self.__user.declineRequest(self.__UserRequesterID, self.__user.getUserID())
        declineMessage = f"Your request to be friends with {UserRequestUsername} has been declined."
        self.__DataHandler.addNotification(self.__UserRequesterID, declineMessage)
        self.__Prompt(f"You have declined {UserRequestUsername}'s request to be your friend.")

        self.__reloadViewFriends()

    def __changeUserIndex(self, direction):
        if direction == "-":
            self.__RequestIndex -=1
        elif direction == "+":
            self.__RequestIndex +=1

        if self.__RequestIndex >= self.__numberOfRequests:
            self.__RequestIndex = 0
        elif self.__RequestIndex < 0:
            self.__RequestIndex = self.__numberOfRequests - 1

        print(self.__UserRequests)
        self.__UserRequesterID = self.__UserRequests[self.__RequestIndex][0]
        UserRequestInfo = self.__DataHandler.getDetaForLogin(self.__UserRequesterID)
        RequestedUser = User(UserRequestInfo)
        UserRequestAvatar = RequestedUser.getAvatar()

        print((self.__UserRequesterID, UserRequestAvatar, UserRequestInfo))

        UserRequestUsername = RequestedUser.getUsername()

        AvatarURL = self.__DataHandler.getAvatarURL(UserRequestAvatar)
        self.__DirectoryHandler.changeDirectoryToAvatar2()
        AvatarPhotoImage = PhotoImage(file=AvatarURL)
        self.__DirectoryHandler.changeDirectoryToMain()
        self.__AvatarPlaceHolderRequest['image'] = AvatarPhotoImage
        self.__AvatarPlaceHolderRequest.image = AvatarPhotoImage

        self.__AccountInfoPlaceHolder['text'] = UserRequestUsername


    def __viewFriends(self):
        self.__ColourButton(self.__ViewFriendsButton)
        self.__viewFriendsFrame, self.__viewFriendsTitle = self.__createFriendsFrame("View Friends")

        self.__numberOfFriends = self.__user.getNumberOfFriends()

        fontStyle = (self.__FontFamily[0], self.__FontSize[7])
        self.__NoOfFriendsLabel = Label(self.__viewFriendsFrame, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(), font=fontStyle)
        self.__NoOfFriendsLabel.place(relx=.05, rely=.45)

        if self.__numberOfFriends == 0:
            self.__NoOfFriendsLabel['text'] = 'It appears you have no friends!\nClick the View Friends tab to add some!'
        else:
            if self.__numberOfFriends == 1:
                self.__NoOfFriendsLabel['text'] = 'You have 1 friend'
            else:
                self.__NoOfFriendsLabel['text'] = f'You have {self.__numberOfFriends} friends'

            self.__NoOfFriendsLabel.place(relx=.051, rely=.25)

            buttonFont = (self.__FontFamily[0], int(round(self.__FontSize[7] * 1.5)))
            self.__LeftButton = Button(self.__viewFriendsFrame, text="<", bd=0, font=buttonFont, bg=self.__Theme.getBackground1(),
                                     command=lambda: self.__changeFriendIndex("-"), cursor="hand2")
            self.__LeftButton.place(relx=.05, rely=.6)

            self.__RightButton = Button(self.__viewFriendsFrame, text=">", bd=0, font=buttonFont, bg=self.__Theme.getBackground1(),
                                      command=lambda: self.__changeFriendIndex("+"), cursor="hand2")
            self.__RightButton.place(relx=.9, rely=.6)

            self.__FriendsPlaceHolder = Frame(self.__viewFriendsFrame, bg=self.__Theme.getBackground3())
            self.__FriendsPlaceHolder.place(relx=.15, rely=.45, width=.7*.63*self.__canvasWidth,
                                      height=.63*.4*self.__canvasHeight)

            self.__PictureLabel = Label(self.__FriendsPlaceHolder)
            self.__PictureLabel.place(relx=0, rely=0)

            fontStyle = (self.__FontFamily[1], self.__FontSize[7])
            self.__FriendsInfoPlaceHolder = Label(self.__FriendsPlaceHolder, bg=self.__Theme.getBackground3(), fg=self.__Theme.getForeground1(), font=fontStyle)
            self.__FriendsInfoPlaceHolder.place(relx=(200 / (.63 * 1366)) + .15, rely=0)
            
            self.__viewFriendsIndex = 0
            self.__Friends = self.__user.getMyFriends()
            FriendInformation = self.__DataHandler.getDetaForLogin(self.__Friends[self.__viewFriendsIndex][0])
            Friend = User(FriendInformation)
            FriendUsername = Friend.getUsername()
            FriendAvatar = Friend.getAvatar()

            AvatarURL = self.__DataHandler.getAvatarURL(FriendAvatar)

            self.__DirectoryHandler.changeDirectoryToAvatar2()
            FriendPhotoImage = PhotoImage(file=AvatarURL)
            self.__DirectoryHandler.changeDirectoryToMain()
            self.__PictureLabel['image'] = FriendPhotoImage
            self.__PictureLabel.config(image=FriendPhotoImage)
            self.__PictureLabel.image = FriendPhotoImage

            self.__FriendsInfoPlaceHolder['text'] = FriendUsername

    def __changeFriendIndex(self, direction):
        if direction == "-":
            self.__viewFriendsIndex -= 1
        elif direction == "+":
            self.__viewFriendsIndex += 1

        if self.__viewFriendsIndex > self.__numberOfFriends:
            self.__viewFriendsIndex = 0
        elif self.__viewFriendsIndex < 0:
            self.__viewFriendsIndex = self.__numberOfFriends - 1

        FriendInformation = self.__DataHandler.getDetaForLogin(self.__Friends[self.__viewFriendsIndex][0])
        Friend = User(FriendInformation)
        FriendUsername = Friend.getUsername()
        FriendAvatar = Friend.getAvatar()

        AvatarURL = self.__DataHandler.getAvatarURL(FriendAvatar)

        self.__DirectoryHandler.changeDirectoryToAvatar2()
        FriendPhotoImage = PhotoImage(file=AvatarURL)
        self.__DirectoryHandler.changeDirectoryToMain()
        self.__PictureLabel['image'] = FriendPhotoImage
        self.__PictureLabel.config(image=FriendPhotoImage)
        self.__PictureLabel.image = FriendPhotoImage

        self.__FriendsInfoPlaceHolder['text'] = FriendUsername

    def __findFriends(self):
        self.__ColourButton(self.__FindFriendsButton)
        self.__findFriendsFrame, self.__findFriendsTitle = self.__createFriendsFrame("Find Friends")

        fontStyle = (self.__FontFamily[1], self.__FontSize[6])
        self.__SearchBox = Entry(self.__findFriendsFrame, font=fontStyle, bd=1, relief="solid")
        self.__SearchBox.place(relx=.05, rely=.35)

        ArrowFont = (self.__FontFamily[1], int(round(self.__FontSize[7] * 0.5))  )

        self.__UpArrow = Label(self.__findFriendsFrame, text=" ▲ ", font=ArrowFont, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1())


        self.__DownArrow = Label(self.__findFriendsFrame, text=" ▼ ", font=ArrowFont, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1())


        self.__AccountFoundPlaceHolder = Message(self.__findFriendsFrame, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(), font=fontStyle,
                                               width=int(round(400 * (self.__canvasWidth / 1366))) )
        self.__AccountFoundPlaceHolder.place(relx=.05, rely=.6, width= .9*.63*self.__canvasWidth,
                                           height=.5*.2*self.__canvasHeight)
        self.__AccountFoundPlaceHolder['text'] = "Enter in username"

        fontStyle = (self.__FontFamily[0], self.__FontSize[6], "underline")
        self.__Request = Button(self.__findFriendsFrame, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(), font=fontStyle, text="Request",
                              bd=1, relief="solid", padx=5, pady=5)
        self.__Request.place(relx=.7, rely=.15)

        self.__SearchBox.bind("<Key>", lambda event: self.__IIfindFriends(event))

    def __IIfindFriends(self, event):
        searchKeyword = self.__SearchBox.get()

        self.__usersFound = self.__user.findUser(searchKeyword)

        if self.__usersFound != []:
            if searchKeyword.strip(" ") == "":
                self.__AccountFoundPlaceHolder['text'] = "Enter in username"
                self.__Request.config(command=lambda: self.__BlankMethod())

                self.__UpArrow.place_forget()
                self.__DownArrow.place_forget()

                return

            self.__friendIndex = 0
            self.__AccountFoundPlaceHolder['text'] = self.__usersFound[self.__friendIndex][1]
            self.__AccountFoundPlaceHolder.bind("<MouseWheel>", lambda event: self.__IIIINextFriend(event))
            self.__Request.config(command=lambda: self.__RequestForFriendship())

            self.__UpArrow.place(relx=0, rely=.55, width=.625 * self.__canvasWidth)
            self.__DownArrow.place(relx=0, rely=.8, width=.625 * self.__canvasWidth)

        else:
            self.__AccountFoundPlaceHolder['text'] = "No such account"
            self.__Request.config(command=lambda: self.__BlankMethod())

            self.__UpArrow.place_forget()
            self.__DownArrow.place_forget()

    def __IINextFriend(self, event):
        self.__friendIndex += 1
        if self.__friendIndex == len(self.__usersFound):
            self.__friendIndex = 0

        self.__AccountFoundPlaceHolder['text'] = self.__usersFound[self.__friendIndex][1]

    def __RequestForFriendship(self):
        alreadyFriends = self.__DataHandler.checkFreindShip(self.__user.getUserID(), self.__usersFound[self.__friendIndex][0])
        if alreadyFriends == True:
            self.__Prompt(f"You are already friends with {self.__usersFound[self.__friendIndex][1]}")
            return
        else:
            self.__DataHandler.sendRequest(self.__user.getUserID(), self.__usersFound[self.__friendIndex][0])
            self.__Prompt(f"You have requested to be friends with {self.__usersFound[self.__friendIndex][1]}!")

    def __createFrame(self, title):
        newFrame = Frame(self.__InfoCanvas, bg=self.__Theme.getBackground1())
        newFrame.place(relx=.3, rely=0, width=.7 * self.__canvasWidth, height=self.__canvasHeight)

        fontStyle = (self.__FontFamily[0], self.__FontSize[3])

        newFrameTitle = Label(newFrame, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(), text=title, font=fontStyle)
        newFrameTitle.place(relx=.05, rely=.05)

        return newFrame, newFrameTitle

    def __createFriendsFrame(self, title):
        newFrame = Frame(self.__FriendsFrame, bg=self.__Theme.getBackground1(), relief="solid", bd=1)
        newFrame.place(relx=.05, rely=.335, width=.63 * self.__canvasWidth, height=.5*self.__canvasHeight)

        fontStyle = (self.__FontFamily[0], self.__FontSize[5])

        newFrameTitle = Label(newFrame, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(), text=title, font=fontStyle)
        newFrameTitle.place(relx=.05, rely=.05)

        return newFrame, newFrameTitle

    def __IIGenerateUsernameKey(self, username):
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

    def __checkChangeUsername(self, username):
        usernameNotBlankMessage = "Username cannot be blank"
        errorMessage = "This username is already taken"
        oldUserID = self.__user.getUserID()
        userID = self.__IIGenerateUsernameKey(username)

        if username.strip(" ") == "":
            self.__IIDisplayError(usernameNotBlankMessage)
            return

        'Create a tree for all usernames and check if the same if so display error message'
        userIDs = self.__DataHandler.getUserIDs()
        usernameTree = Tree(userIDs)
        found = usernameTree.Search(userID)
        print("FOUND MATCHES", found)

        if found == True:
            self.__IIDisplayError(errorMessage)
            return
        elif found == False:
            print((userID,  username))
            self.__user.changeUsername(userID,  username)
            self.__Prompt(f"Username is changed to {username}")


    def __checkChangePassword(self, password, confirmPassword):
        userID = self.__user.getUserID()
        noMatchMessage = "Passwords do not match"
        shortPassowrdMessage = "Password must be at least 6 digits longs"

        if password != confirmPassword:
            self.__IIDisplayError(noMatchMessage)
            return

        if len(password) < 6:
            self.__IIDisplayError(shortPassowrdMessage)
            return

        self.__user.changePassword(confirmPassword)
        self.__IIDisplayMessage("Password is changed")

    def __changeAvatarIndex(self, Direction):
        if Direction == "+":
            self.__avatarIndex +=1
        elif Direction == "-":
            self.__avatarIndex -= 1

        if self.__avatarIndex == -1:
            self.__avatarIndex = 11

        if self.__avatarIndex == 12:
            self.__avatarIndex = 0


        NewAvatarFile = self.__avatars[self.__avatarIndex][1]
        self.__DirectoryHandler.changeDirectoryToAvatar()
        NextPhotoImage = PhotoImage(file=NewAvatarFile)
        self.__DirectoryHandler.changeDirectoryToMain()
        self.__AvatarPlaceHolder['image'] = NextPhotoImage
        self.__AvatarPlaceHolder.image = NextPhotoImage

        self.__AvatarPricePlaceHolder['text'] = str(self.__avatars[self.__avatarIndex][2]) + " coins"

    def __buy(self):
        self.__user.changeAvatar(self.__avatars[self.__avatarIndex][0])
        print(self.__user.getAvatar())
        coins = self.__user.getCoins()
        if coins >= self.__avatars[self.__avatarIndex][2]:
            self.__user.changeCoins(-self.__avatars[self.__avatarIndex][2])
            newCoins = self.__user.getCoins()
            self.__Prompt(f"You now have {newCoins} coins")
        else:
            self.__Prompt("Not enough money")


    def __Prompt(self, text):
        self.__PromptFrame = Frame(self.__InfoCanvas, bg=self.__Theme.getBackground3())
        self.__PromptFrame.place(relx=.4, rely=.3, width=.5*self.__screenWidth, height=.4*self.__screenHeight)

        fontStyle = (self.__FontFamily[0], int(round(self.__FontSize[7] * 1.5)))
        self.__PromptText = Message(self.__PromptFrame, bg=self.__Theme.getBackground3(), fg=self.__Theme.getForeground1(), text=text, font = fontStyle,
                                  width=int(round(300*(self.__screenWidth / 1366))))
        self.__PromptText.place(relx=.05, rely=.25, width=.45*self.__screenWidth,
                              height=.5*.45*self.__screenHeight)

        fontStyle = (self.__FontFamily[0], int(round(self.__FontSize[7])))
        self.__ExitButton = Button(self.__PromptFrame, text= " x ", font= fontStyle, bg="black", fg="white",
                                 command= lambda: self.__exitPrompt())
        self.__ExitButton.place(relx=.9, rely=0, width=.05*self.__screenWidth, height=.05*self.__screenWidth)

    def __CreateFormEntry(self, frame, text, relY, password):
        fontStyle = (self.__FontFamily[0], self.__FontSize[6])
        TextLabel = Label(frame, text=text, font=fontStyle, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1())
        TextLabel.place(relx=.05, rely=relY)

        TextEntry = Entry(frame, font=fontStyle, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1())
        TextEntry.place(relx=.05, rely=relY + 0.1, width=.7*.9*self.__canvasWidth)

        fontStyle = (self.__FontFamily[0], self.__FontSize[7], "underline")
        FormButton = Button(frame, text=" OK ", font=fontStyle, bd=1, cursor="hand2", bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(),
                            relief="solid", activebackground="white", padx=5, pady=5)
        FormButton.place(relx=.825, rely=relY, width=.075*.9*self.__screenWidth)

        if password == True:
            TextEntry.config(show="⚫")

        return TextLabel, TextEntry, FormButton

    def __exitPrompt(self):
        self.__PromptFrame.destroy()

    def __IIDisplayError(self, text):
        '''Displays Error at the bottom of the frame based on the situation'''
        fontStyle = (self.__FontFamily[0], self.__FontSize[7])
        errorWidget = Label(self.__ChangeLoginFrame, text=text, bg=self.__Theme.getBackground1(), fg="red", font=fontStyle)
        errorWidget.place(relx=.05, rely=.925)

    def __IIDisplayMessage(self, text):
        '''Displays Error at the bottom of the frame based on the situation'''
        fontStyle = (self.__FontFamily[0], self.__FontSize[7])
        errorWidget = Label(self.__ChangeLoginFrame, text=text, bg=self.__Theme.getBackground1(), fg=self.__Theme.getForeground1(), font=fontStyle)
        errorWidget.place(relx=0, rely=.925)

    def __BlankMethod(self):
        pass

if __name__ in '__main__':
    Main = Settings()