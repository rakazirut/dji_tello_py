from djitellopy import tello
from time import sleep

def initDrone():
    me = tello.Tello()
    me.connect()
    return me