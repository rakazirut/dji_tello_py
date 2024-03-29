import Helpers.KeyPressFunctions as kp
import Helpers.HelperFunctions as hf
import cv2
import time

global img

me = hf.initDrone()
kp.init()
me.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kp.getKey('LEFT'): lr = -speed
    elif kp.getKey('RIGHT'): lr = speed 

    if kp.getKey('UP'): fb = speed
    elif kp.getKey('DOWN'): fb = -speed
    
    if kp.getKey('w'): ud = speed
    elif kp.getKey('s'): ud = -speed

    if kp.getKey('a'): yv = -speed
    elif kp.getKey('d'): yv = speed

    if kp.getKey('i'): me.flip_forward()
    if kp.getKey('k'): me.flip_back()
    if kp.getKey('j'): me.flip_left()
    if kp.getKey('l'): me.flip_right()


    if kp.getKey('q'): me.land()
    if kp.getKey('e'): me.takeoff()

    if kp.getKey('z'): 
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)

    if kp.getKey('b'):
        print(me.get_current_state())

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.putText(img, '{}% battery'.format(me.get_battery()), (5,230), cv2.FONT_HERSHEY_PLAIN,
                    1, (255, 255, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)