# > this file will mainly be used to handle variables and variable operations again so I am not hardcoding anything within the main file
import settings

def calcHeight(percent):
    return (settings.mainH / 100) * percent

def calcWidth(percent):
    return (settings.mainW / 100) * percent