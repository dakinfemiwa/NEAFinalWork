import os
try:
    os.chdir(os.getcwd() + "\\Tools")
except:
    pass
import random

class Question:
    def __init__(self, type, mC):
        self.__Type = type
        self.__MultipleChoice = mC

        self.__GenerateQuestion()

    def __GenerateQuestion(self):
        if self.__Type == "projectile":
            t = random.randint(1, 78)
            t /= 10
            self.__correctAnswer = t * 10
            self.__QuestionStr = f"An object is dropped from rest. Find the speed of the object if t={t}s and g=10ms¯²"

        elif self.__Type == "speed":
            #Determines what variable will be asked
            variables = ["speed", "distance", "time"]
            random.shuffle(variables)
            variableTBCalculated = variables[0]


            #Generates components for the question and the correct answer
            if variableTBCalculated == "speed":
                speed = random.randint(1, 15)
                time = random.randint(1, 15)
                distance = speed * time

                self.__correctAnswer = speed
                variableUnit = ["ms¯¹"]

            elif variableTBCalculated == "distance":
                speed = random.randint(1, 15)
                time = random.randint(1, 15)
                distance = speed * time

                self.__correctAnswer = distance
                variableUnit = ["m"]

            elif variableTBCalculated == "time":
                speed = random.randint(1, 15)
                time = random.randint(1, 15)
                distance = speed * time

                self.__correctAnswer = time
                variableUnit = ["s"]

            variableArray = [self.__correctAnswer]


            #String operations for variables
            for index in range(2):
                if variables[index + 1] == "speed":
                    variableArray.append(speed)
                    variableUnit.append("ms¯¹")
                elif variables[index + 1] == "distance":
                    variableArray.append(distance)
                    variableUnit.append("m")
                elif variables[index + 1] == "time":
                    variableArray.append(time)
                    variableUnit.append("s")

            self.__QuestionStr = f"Find the {variableTBCalculated} in {variableUnit[0]} if the {variables[1]} is {variableArray[1]}{variableUnit[1]} and the {variables[2]} is {variableArray[2]}{variableUnit[2]}"

        elif self.__Type == "diffrentiation":
            # Randomly generates polynomial by deducing its coefficient and degree
            QuestionCoefficient = random.randint(1, 16)
            QuestionPolynomialDegree = random.randint(1, 8)

            # Converts question into expressible string form readable by humans
            ExpressionStr = self.__ConvertToString(QuestionCoefficient, QuestionPolynomialDegree)

            # Generates answer for question
            AnswerCoefficient = QuestionCoefficient * QuestionPolynomialDegree
            AnswerPolynomialDegree = QuestionPolynomialDegree - 1

            #Creates string form depending on whether question is multiple choice or standard
            if self.__MultipleChoice == False:
                if AnswerPolynomialDegree == 1:
                    if AnswerCoefficient != 1:
                        answerString = str(AnswerCoefficient) + "x"
                    else:
                        answerString = "x"
                else:
                    if AnswerCoefficient != 1:
                        answerString = str(AnswerCoefficient) + "x^" + str(AnswerPolynomialDegree)
                    else:
                        answerString = "x^" + str(AnswerPolynomialDegree)
            else:
                answerString = self.__ConvertToString(AnswerCoefficient, AnswerPolynomialDegree)

            self.__QuestionStr = f"What is the diffrential of {ExpressionStr} with respect to x?"
            self.__correctAnswer = answerString

        elif self.__Type == "integration":
            # Randomly generates polynomial by deducing its coefficient and degree
            AnswerCoefficient = random.randint(1, 16)
            AnswerPolynomialDegree = random.randint(1, 8)

            # Creates string form depending on whether question is multiple choice or standard
            if self.__MultipleChoice == False:
                if AnswerPolynomialDegree == 1:
                    if AnswerCoefficient != 1:
                        answerString = str(AnswerCoefficient) + "x"
                    else:
                        answerString = "x"
                else:
                    if AnswerCoefficient != 1:
                        answerString = str(AnswerCoefficient) + "x^" + str(AnswerPolynomialDegree)
                    else:
                        answerString = "x^" + str(AnswerPolynomialDegree)
            else:
                answerString = self.__ConvertToString(AnswerCoefficient, AnswerPolynomialDegree)

            # Generates answer for question
            QuestionCoefficient = AnswerCoefficient * AnswerPolynomialDegree
            QuestionPolynomialDegree = AnswerPolynomialDegree - 1

            # Converts question into expressible string form readable by humans
            ExpressionStr = self.__ConvertToString(QuestionCoefficient, QuestionPolynomialDegree)

            self.__QuestionStr = f"Find ∫ {ExpressionStr} dx"
            self.__correctAnswer = answerString + "+c"

        elif self.__Type == "momentum":
            variables = ["momentum", "velocity"]
            random.shuffle(variables)

            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            random.shuffle(numbers)
            velocity = numbers[0]
            players = ['Porzingis', 'Lebron', 'Steph Curry']
            random.shuffle(players)
            player = players[0]
            momentum = 0.6 * velocity


            if variables[0] == "momentum":
                self.__correctAnswer = momentum
                unit = "ms¯¹"
                variableOther = "{:.2f}".format(velocity)
            else:
                self.__correctAnswer = velocity
                unit = "kgms¯¹"
                variableOther = "{:.2f}".format(momentum)


            self.__QuestionStr = f"As {player} plays handles the ball (mass=0.6kg) with a {variables[1]} of {variableOther}{unit}, find the {variables[0]} of the ball."

        if self.__MultipleChoice == True and (self.__Type == "diffrentiation" or self.__Type == "integration" ) == False:
            self.__optionsArray = [self.__correctAnswer]
            for option in range(2):
                difference = [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7]
                random.shuffle(difference)
                wrongOption = self.__correctAnswer + difference[1]
                self.__optionsArray.append(wrongOption)

        elif self.__Type == "diffrentiation" or self.__Type == "integration":
            self.__optionsArray = [self.__correctAnswer]
            difference = [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7]
            for option in range(2):
                random.shuffle(difference)
                wrongCoefficient = AnswerCoefficient - difference[0]
                random.shuffle(difference)
                wrongPolynomialDegree = AnswerPolynomialDegree - difference[0]

                wrongOption = self.__ConvertToString(wrongCoefficient, wrongPolynomialDegree)

                self.__optionsArray.append(wrongOption)

        random.shuffle(self.__optionsArray)
        self.__correctOption = self.__optionsArray.index(self.__correctAnswer)

    def GetQuestion(self):
        if self.__MultipleChoice == True:
            # Return question in string, correct answer, options, and lane number for right
            return self.__QuestionStr, self.__correctAnswer, self.__optionsArray, int(self.__correctOption + 1)
        elif self.__MultipleChoice == False:
            return self.__QuestionStr, self.__correctAnswer

    def __ConvertToString(self, coefficient, degree):
        #Adds the power to the polynomial experssions
        if coefficient != 1:
            string = str(coefficient) + "x"
        else:
            string = "x"

        if degree == 2:
            string += "²"
        elif degree == 3:
            string += "³"
        elif degree == 4:
            string += "⁴"
        elif degree == 5:
            string += "⁵"
        elif degree == 6:
            string += "⁶"
        elif degree == 7:
            string += "⁷"
        elif degree == 8:
            string += "⁸"
        elif degree == 0:
            string = str(coefficient)

        return string

if __name__ in '__main__':
    Main = RunGameEp1()