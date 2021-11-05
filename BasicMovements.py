from djitellopy import tello
from time import sleep
import HelperFunctions as hf

me = hf.initDrone()

me.takeoff()
me.send_rc_control(0, 50, 0, 0)
sleep(2)
me.send_rc_control(30, 0, 0, 0)
sleep(2)
me.send_rc_control(0, 0, 0, 0)
me.land()
