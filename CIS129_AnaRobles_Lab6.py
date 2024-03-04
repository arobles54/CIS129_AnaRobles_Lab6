# Lab 6 The Hotdog Cookout Lab
# Author: Ana Robles
# Date: 03/03/2024
# Description: This program calculates how many hotdog ingredients needed and how many are left over.

def getTotalHotDogs():
    attendees = int(input("How many guests?: "))
    hotDogs = int(input("How many hotdogs given to each guest?: "))
    total = attendees * hotDogs
    return total

def showResults(totalHotDogs):
    DOGS = 10
    BUNS = 8
    
    dogsLeft = (DOGS - totalHotDogs % DOGS) % DOGS
    minDogs = (totalHotDogs // DOGS) + (0 ** (0 ** dogsLeft))
    
    bunsLeft = (BUNS - totalHotDogs % BUNS) % BUNS
    minBuns = (totalHotDogs // BUNS) + (0 ** (0 ** bunsLeft))
    
    print("Minimum packages of hot dogs needed", minDogs)
    print("Minimum packages of hot dog buns needed", minBuns)
    print("Hot dogs remaining", dogsLeft)
    print("Hot dog buns remaining", bunsLeft)
    
# Call the functions
totalHotDogs = getTotalHotDogs()
showResults(totalHotDogs)


    
    
    



