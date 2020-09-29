import os
orignialDir = os.getcwd()
try:
    os.chdir(os.getcwd() + "\\Tools")
except:
    pass
from Stack import Stack
os.chdir(orignialDir)
import sqlite3
from DirectoryHandler import DirectoryHandler

#Module used to handle all the data regarding teh database
class DataHandler:
    def __init__(self):
        #The directory need to be changed to the /Main folder so this part of the program uses the DirectoryHandler
        #   module to change it
        self.__DirectoryHandler = DirectoryHandler()
        self.__DirectoryHandler.changeDirectoryToMainFolder()
        #Sets up a connection with teh database
        self.__conn = sqlite3.connect("educationalGameDatabase.db")
        #Resets the directory back to the original directory
        self.__DirectoryHandler.changeDirectoryToMain()
        #Sets a value to the cursor so it can execute SQLite3 statements
        self.__cursor = self.__conn.cursor()

    #Module to get a record for a specific userID
    def getDetaForLogin(self, userID):
        #Executes query for record
        self.__cursor.execute("SELECT * FROM User WHERE UserID = ?", (userID,))
        #Returns record for the specific UserID
        return self.__cursor.fetchall()

    #Module to add a user's data to the datatbase or to sign up the user
    def addUserDetails(self, userKey, username, password):
        #Inserts the UserID, username, password into the database (as well as giving 0 points)
        self.__cursor.execute("INSERT INTO User VALUES(?, ?, ?, ?)", (userKey, username, password, 0))
        #Updates database by committinng to it
        self.__conn.commit()
        #Inserts Avatar to user
        self.__cursor.execute("INSERT INTO AvatarUser VALUES(?, ?)", (userKey, "Coach"))
        self.__conn.commit()
        #Inserts Activity to user
        self.__cursor.execute("INSERT INTO Activity VALUES(?, ?)", (userKey, 5))
        self.__conn.commit()

    #Module to change an user details i.e. password
    def changeUserDetails(self, userID, fieldName, value):
        #Executes UPDATE command to database
        self.__cursor.execute(f"UPDATE User SET {fieldName} TO ?", (value,))

    # Module to get all userIDs for login validation
    def getUserIDs(self):
        #Execuutes query for all records
        self.__cursor.execute("SELECT * FROM User")
        #The aim is to get all UserIDs in array format
        #A blank array is set
        userIDs = []
        #This is the form of the data returned from query
        userID = self.__cursor.fetchall()
        #Appends the value in the UserID field for the User table
        for user in userID:
            userIDs.append(user[0])
        #Returns array with newly appended UserIDs
        return userIDs

    #Used to collect data for the settings area
    def getCoins(self, userID):
        wholeArray = self.getDetaForLogin(userID)
        return wholeArray[0][3]

    #Used to increase the score for the user
    def increaseCoins(self, userID, coins):
        #calls UPDATE command
        self.__cursor.execute("UPDATE User SET Coins = ? WHERE UserID=?", (coins, userID))
        #Commits change- saves changes to the database
        self.__conn.commit()

    #Used to increase the score for the user
    def getActivity(self, userID, ):
        #Query to find activity score
        self.__cursor.execute("SELECT ActivityNo FROM Activity WHERE UserID = ?", (userID,))
        #Returns value from query
        return self.__cursor.fetchone()

    def getAvatarInfo(self):
        self.__cursor.execute("SELECT * FROM Avatar ORDER BY Cost" )
        return self.__cursor.fetchall()

    def getAvatarURL(self, avatarName):
        self.__cursor.execute("SELECT ImageURL FROM Avatar WHERE AvatarName = ?", (avatarName,))
        return self.__cursor.fetchall()

    def getUserAvatar(self, userID):
        #Query to find activity score
        self.__cursor.execute("SELECT AvatarName FROM AvatarUser WHERE UserID = ?", (userID,))
        #Returns value from query
        return self.__cursor.fetchall()

    def changeAvatar(self, userID, newAvatar):
        #calls UPDATE command
        self.__cursor.execute("UPDATE AvatarUser SET AvatarName = ? WHERE UserID=?", (newAvatar, userID))
        #Commits change- saves changes to the database
        self.__conn.commit()

    #Changes Username
    def changeUserID(self, userID, newuserID, newUsername):
        #calls UPDATE command
        self.__cursor.execute("UPDATE User SET UserID =?, Username = ? WHERE UserID=?", (newuserID, newUsername, userID))
        #Commits change- saves changes to the database
        self.__conn.commit()
        #calls UPDATE command
        self.__cursor.execute("UPDATE AvatarUser SET UserID =? WHERE UserID=?", (newuserID, userID))
        #Commits change- saves changes to the database
        self.__conn.commit()
        #calls UPDATE command
        self.__cursor.execute("UPDATE Activity SET UserID =? WHERE UserID=?", (newuserID, userID))
        #Commits change- saves changes to the database
        self.__conn.commit()
        # calls UPDATE command
        self.__cursor.execute("UPDATE Friends SET Player1 =? WHERE Player1=?", (newuserID, userID))
        #Commits change- saves changes to the database
        self.__conn.commit()
        # calls UPDATE command
        self.__cursor.execute("UPDATE Friends SET Player2 =? WHERE Player2=?", (newuserID, userID))
        #Commits change- saves changes to the database
        self.__conn.commit()
        # calls UPDATE command
        self.__cursor.execute("UPDATE Requests SET Requester =? WHERE Requester=?", (newuserID, userID))
        #Commits change- saves changes to the database
        self.__conn.commit()
        # calls UPDATE command
        self.__cursor.execute("UPDATE Requests SET Responder=? WHERE Responder=?", (newuserID, userID))
        #Commits change- saves changes to the database
        self.__conn.commit()
        # calls UPDATE command
        self.__cursor.execute("UPDATE Notifications SET UserID=? WHERE UserID=?", (newuserID, userID))
        #Commits change- saves changes to the database
        self.__conn.commit()

    #Changes Password
    def changePassword(self, userID, newPassword):
        print(newPassword, "password")
        #calls UPDATE command
        self.__cursor.execute("UPDATE User SET Password=? WHERE UserID=?", (newPassword, userID,))
        #Commits change- saves changes to the database
        self.__conn.commit()

    def returnNumberOfFriends(self, userID):
        self.__cursor.execute("SELECT COUNT(*) FROM Friends WHERE Player1=?", (userID,))
        return self.__cursor.fetchone()[0]

    def addFriends(self, user1ID, user2ID):
        self.__cursor.execute("INSERT INTO Friends VALUES(?, ?)", (user1ID, user2ID))
        self.__conn.commit()

        self.__cursor.execute("INSERT INTO Friends VALUES(?, ?)", (user2ID, user1ID))
        self.__conn.commit()

    def findUser(self, keyword):
        self.__cursor.execute("SELECT * FROM User WHERE Username LIKE ?", (keyword+'%',))
        return self.__cursor.fetchall()

    def checkFreindShip(self, userID1, userID2):
        self.__cursor.execute("SELECT * FROM Friends WHERE Player1=? AND Player2=?", (userID1, userID2))
        if self.__cursor.fetchall() == []:
            return False
        else:
            return True

    def sendRequest(self, userID1, userID2):
        self.__cursor.execute("INSERT INTO Requests VALUES(?, ?)", (userID1, userID2))
        self.__conn.commit()

    def getRequest(self, userID):
        self.__cursor.execute("SELECT * FROM Requests WHERE Responder=?", (userID,))
        return self.__cursor.fetchall()

    def getNumberOfRequests(self, userID):
        self.__cursor.execute("SELECT COUNT(*) FROM Requests WHERE Responder=?", (userID,))
        return self.__cursor.fetchone()[0]

    def addFriendship(self, userID1, userID2):
        self.__cursor.execute("DELETE FROM Requests WHERE Requester=? AND Responder=?", (userID1, userID2))
        self.__conn.commit()
        self.__cursor.execute("INSERT INTO Friends VALUES(?, ?)", (userID1, userID2))
        self.__conn.commit()
        self.__cursor.execute("INSERT INTO Friends VALUES(?, ?)", (userID2, userID1))
        self.__conn.commit()

    def declineRequest(self, userID1, userID2):
        self.__cursor.execute("DELETE FROM Requests WHERE Requester=? AND Responder=?", (userID1, userID2))
        self.__conn.commit()

    def removeFriendship(self, userID1, userID2):
        self.__cursor.execute("DELETE FROM Friends WHERE Player1=? AND Player2=?", (userID1, userID2))
        self.__conn.commit()
        self.__cursor.execute("DELETE FROM Friends WHERE Player1=? AND Player2=?", (userID2, userID1))
        self.__conn.commit()

    def addNotification(self, userID, notification):
        self.__cursor.execute("INSERT INTO Notifications VALUES(?, ?)", (userID, notification))
        self.__conn.commit()

    def getNotifications(self, userID):
        self.__cursor.execute("SELECT Notification FROM Notifications WHERE UserID=?", (userID,))
        return self.__cursor.fetchall()

    def clearNotifications(self, userID):
        self.__cursor.execute("DELETE FROM Notifications WHERE UserID=?", (userID,))
        self.__conn.commit()

    def getUserFriends(self, userID):
        self.__cursor.execute("SELECT Player2 FROM Friends WHERE Player1=?", (userID,))
        return self.__cursor.fetchall()

    def getGameHighscore(self, userID):
        self.__cursor.execute("SELECT MAX(Points) FROM BasketballGameStats WHERE UserID=?", (userID,))
        return self.__cursor.fetchall()

    def storeBasketballScore(self, userID, score):
        self.__cursor.execute("INSERT INTO BasketballGameStats VALUES(?, ?)", (userID, score))
        self.__conn.commit()

    def getAverageScore(self, userID):
        self.__cursor.execute("SELECT AVG(Points) FROM BasketballGameStats WHERE UserID=?", (userID,))
        return self.__cursor.fetchone()[0]

    def addSwimTime(self, userID, time):
        self.__cursor.execute("INSERT INTO SwimmingTimes VALUES(?, ?)", (userID, time))
        self.__conn.commit()

    def getFastestTimeForUser(self, userID):
        self.__cursor.execute("SELECT MIN(Time) FROM SwimmingTimes WHERE UserID=?", (userID,))
        return self.__cursor.fetchone()[0]

    def getFastestTime(self):
        self.__cursor.execute("SELECT MIN(*) FROM SwimmingTimes")
        return self.__cursor.fetchone()[0]