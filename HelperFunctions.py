from djitellopy import tello
from time import sleep

def initDrone():
    me = tello.Tello()
    me.connect()
    print(me.get_battery())
    return me