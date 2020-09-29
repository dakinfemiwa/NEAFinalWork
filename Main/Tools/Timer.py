import datetime
import time

class Timer:
    def __init__(self):
        self.__TimeChange = 0

    def StartTimer(self, canvas):
        self.__Stop = False
        self.__StartTime = time.time()
        self.__Time(canvas)

    def __Time(self, canvas):
        self.__NewTime = time.time()
        self.__TimePassed = self.__NewTime - self.__StartTime


        if self.__Stop == False:
            canvas.after(75, lambda: self.__Time(canvas))

    def StopTimer(self):
        self.__Stop = True

    def GetTime(self):
        self.__TimePassedStr = "{:.1f}".format(self.__TimePassed)
        return self.__TimePassedStr