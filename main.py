#Import libraries
import cv2
import mediapipe as mp
from pynput.keyboard import Controller as KeyController, Key
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
from comtypes import CLSCTX_ALL

#Initialize mediapipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

#Volume Control Setup
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

#Keyboard Automation Setup
keyboard = KeyController()

#Gesture Detection Logic
def get_finger_status(lm_list):
    finger_up = []

    finger_up.append(lm_list[4][0] > lm_list[3][0])

    finger_up.append(lm_list[8][1] < lm_list[6][1]) #Index
    finger_up.append(lm_list[12][1] < lm_list[10][1]) #Middle
    finger_up.append(lm_list[16][1] < lm_list[14][1]) #Ring
    finger_up.append(lm_list[20][1] < lm_list[18][1]) #Pinky

    return finger_up

#Perform actions based on gestures
def perform_actions(gesture):
    if gesture == [True,False,False,False,False]: #Thumb Up
        volume.SetMasterVolumeLevelScalar(0.9,None)
        print("Volume Up")
    elif gesture == [False,True,True,False,False]: #Peace Sign
        keyboard.press(Key.ctrl_l)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.release(Key.ctrl_l)
        print("Switched Tab")
    elif gesture == [False,False,False,False,False]: #Fist
        volume.SetMasterVolumeLevelScalar(0.0, None)
        print("Mute")
    elif gesture == [True]*5: #Open palm
        curr_brightness = sbc.get_brightness(display=0)[0]
        sbc.set_brightness(min(curr_brightness + 10,100))
        print("Brightness Up")
        

#Capture Webcam and Detect Hand

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

    result = hands.process(img_rgb)

#Extract landmarks and Chek Gesture
    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        lm_list = []
        for id, lm in enumerate(hand_landmarks.landmark):
            h, w, _ = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lm_list.append((cx, cy))

        if lm_list:
            fingers = get_finger_status(lm_list)
            perform_actions(fingers)

        mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Gesture Control", img)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break
cap.release()
cv2.destroyAllWindows()
