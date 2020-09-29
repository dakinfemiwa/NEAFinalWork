from DataHandler import DataHandler

class User:
    def __init__(self, data):
        #Used to get avatar data from database
        DataHandlerModule = DataHandler()
        #Creates Attributes Relating to user
        self.__userID = data[0][0]
        self.__username = data[0][1]
        self.__password = data[0][2]
        self.__coins = data[0][3]
        self.__avatar = DataHandlerModule.getUserAvatar(self.__userID)[0][0]

    #Gets attributes for users. Looks from database if neccessary
    def getUserID(self):
        return self.__userID

    def getUsername(self):
        return self.__username

    def getCoins(self):
        return self.__coins

    def getPassword(self):
        return self.__password

    def getAvatar(self):
        return self.__avatar

    def getRequests(self):
        DataHandlerModule = DataHandler()
        self.__Requests = DataHandlerModule.getRequest(self.__userID)
        return self.__Requests

    def getNumberOfRequests(self):
        DataHandlerModule = DataHandler()
        self.__RequestsNo = DataHandlerModule.getNumberOfRequests(self.__userID)
        return self.__RequestsNo

    def getNumberOfFriends(self):
        DataHandlerModule = DataHandler()
        self.__NoOfFriends = DataHandlerModule.returnNumberOfFriends(self.__userID)
        return self.__NoOfFriends

    def getMyFriends(self):
        DataHandlerModule = DataHandler()
        self.__MyFriends = DataHandlerModule.getUserFriends(self.__userID)
        return self.__MyFriends

    def findUser(self, searchKeyword):
        DataHandlerModule = DataHandler()
        self.__FoundFriends = DataHandlerModule.findUser(searchKeyword)
        return self.__FoundFriends

    def getHighScore(self):
        DataHandlerModule = DataHandler()
        self.__HighScoreBball = DataHandlerModule.getGameHighscore(self.__userID)
        return self.__HighScoreBball[0][0]

    def getAverageBBallScore(self):
        DataHandlerModule = DataHandler()
        self.__HighScoreBball = DataHandlerModule.getGameHighscore(self.__userID)
        return self.__HighScoreBball

    def getFastestSwimingTime(self):
        DataHandlerModule = DataHandler()
        self.__FastestSwimmingTime = DataHandlerModule.getFastestTimeForUser(self.__userID)
        return self.__FastestSwimmingTime

    #This section involves teh changes of usernames, passwords, or avatars if neccessary
    #   as well as response to friend requests
    def changeUsername(self, newUserID, newUsername):
        oldUsername = self.__userID
        self.__userID = newUserID
        self.__username = newUsername
        DataHandlerModule = DataHandler()
        DataHandlerModule.changeUserID(oldUsername, self.__userID, self.__username)

    def changePassword(self, newPassword):
        self.__password = newPassword
        DataHandlerModule = DataHandler()
        DataHandlerModule.changePassword(self.__userID, self.__password)

    def changeAvatar(self, newAvatar):
        self.__avatar = newAvatar
        DataHandlerModule = DataHandler()
        DataHandlerModule.changeAvatar(self.__userID, self.__avatar)

    def placeScore(self, score):
        DataHandlerModule = DataHandler()
        DataHandlerModule.storeBasketballScore(self.__userID, score)

    def changeCoins(self, change):
        newCoins = self.__coins + change
        self.__coins += change
        DataHandlerModule = DataHandler()
        DataHandlerModule.increaseCoins(self.__userID, self.__coins)

    def acceptRequest(self, secondUser):
        DataHandlerModule = DataHandler()
        DataHandlerModule.addFriendship(secondUser, self.__userID)

    def declineRequest(self, secondUser):
        DataHandlerModule = DataHandler()
        DataHandlerModule.declineRequest(secondUser, self.__userID)

    def removeFriend(self, secondUser):
        DataHandlerModule = DataHandler()
        DataHandlerModule.removeFriendship(secondUser)

    def clearNotifications(self):
        DataHandlerModule = DataHandler()
        DataHandlerModule.clearNotifications(self.__userID)

    def getNotifications(self):
        DataHandlerModule = DataHandler()
        self.__Notifications = DataHandlerModule.getNotifications(self.__userID)
        return self.__Notifications

    def addSwimmingTime(self, time):
        DataHandlerModule = DataHandler()
        DataHandlerModule.addSwimTime(self.__userID, time)