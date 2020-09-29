class Theme():
    def __init__(self, theme="light"):
        self.__theme = theme

        if theme == "light":
            # Backgrounds
            #   Backgrounds of widgets in general
            self.__background1 = "#FFFFFF"
            self.__background2 = "#FAFAFA"
            self.__background3 = "#F0F0F0"
            self.__background3b = "#E0E0E0"
            #   Background of basketball court
            self.__background4 = "#ED7D31"
            #   Background of swimming pool
            self.__background5 = "#ADD8E6"
            #   Background of enemy colour
            self.__background6 = "#FFB6C1"
            #   Background for shifter
            self.__background7 = "#CCCCCC"

            #   Line colour - for pools and for the basketball court
            self.__LineColour = "white"

            # General text foreground
            self.__foreground1 = "#000000"
            # Red text colour for errors
            self.__foreground2 = "#FF0000"

        if theme == "dark":
            #Backgrounds
            #   Backgrounds of widgets in general
            self.__background1 = "black"
            self.__background2 = "#050505"
            self.__background3 = "#0F0F0F"
            self.__background3b = "#BFBFBF"
            #   Background of basketball court
            self.__background4 = "#ED7D31"
            #   Background of swimming pool
            self.__background5 = "#ADD8E6"
            #   Background of enemy colour
            self.__background6 = "red"
            #   Background for shifter
            self.__background7 = "#333333"# "#CCCCCC"

            #   Line colour - for pools and for the basketball court
            self.__LineColour = "white"

            #General text foreground
            self.__foreground1 =  "white"#"#000000"
            #Red text colour for errors
            self.__foreground2 = "#FF0000"

    #Returns colour variations
    def getBackground1(self):
        return self.__background1

    def getBackground2(self):
        return self.__background2

    def getBackground3(self):
        return self.__background3

    def getBackground3b(self):
        return self.__background3b

    def getBackground4(self):
        return self.__background4

    def getBackground5(self):
        return self.__background5

    def getBackground6(self):
        return self.__background6

    def getBackground7(self):
        return self.__background7

    def getForeground1(self):
        return self.__foreground1

    def getForeground2(self):
        return self.__foreground2

    def getLineColour(self):
        return self.__LineColour

    def getTheme(self):
        return self.__theme

    def changeTheme(self, newTheme):
        self.__theme = newTheme
