import csv 
from functools import reduce
import random
import time

randList = []
counter = 0
wrongAnswers = []

def checkRedundancy(randNum):
    global randList, counter
    if(randNum not in randList):
        randList.append(randNum)
        counter+=1
        return True
    else:
        return False

with open('exercise.csv', 'r') as file:
        reader = list(csv.reader(file))
        
        while(counter < 5):
            randomNum = random.randint(0, 13) 
            singelton = checkRedundancy(randomNum)

            if( singelton ):
                start = time.perf_counter() 
                userInput = input(reader[randomNum][0] +  ' + ' + reader[randomNum][1] + ' = ') # user answer
                end = time.perf_counter() 
                print()
                result = reduce((lambda x, y: int(x) + int(y)), reader[randomNum]) # correct answer
                if( int(userInput) == result ):
                    print("Correct!")
                    print()
                else:
                    wrongAnswers.append(reader[randomNum][0] +  ' + ' + reader[randomNum][1] + ' = ' + userInput + '|' + str(end))
                    print("Wrong 🙁 ")
                    print(reader[randomNum][0] +  ' + ' + reader[randomNum][1] + ' = ' + str(result))
                    print()



print(wrongAnswers)